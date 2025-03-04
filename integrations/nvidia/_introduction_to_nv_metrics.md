```python
from dotenv import load_dotenv

load_dotenv()
```




    True




```python
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings


evaluator_llm = LangchainLLMWrapper(ChatOpenAI(model="gpt-4o-mini"))
evaluator_embeddings = LangchainEmbeddingsWrapper(OpenAIEmbeddings(model="text-embedding-3-small"))
```

# Answer Accuracy

**Answer Accuracy** measures the agreement between a model’s response and a reference ground truth for a given question. This is done via two distinct "LLM-as-a-judge" prompts that each return a rating (0, 2, or 4). The metric converts these ratings into a [0,1] scale and then takes the average of the two scores from the judges. Higher scores indicate that the model’s answer closely matches the reference.

- **0** → The **response** is inaccurate or does not address the same question as the **reference**.
- **2** → The **response** partially aligns with the **reference**.
- **4** → The **response** exactly aligns with the **reference**.


```python
from ragas.dataset_schema import SingleTurnSample
from ragas.metrics._nv_metrics import AnswerAccuracy
from ragas.metrics import AnswerAccuracy

sample = SingleTurnSample(
    user_input="When was Einstein born?",
    response="Albert Einstein was born in 1879.",
    reference="Albert Einstein was born in 1879."
)

scorer = AnswerAccuracy(llm=evaluator_llm) # evaluator_llm wrapped with ragas LLM Wrapper
score = await scorer.single_turn_ascore(sample)
print(score)
```

    1.0


### How It’s Calculated

**Step 1:** The LLM generates ratings using two distinct templates to ensure robustness:

- **Template 1:** The LLM compares the **response** with the **reference** and rates it on a scale of **0, 2, or 4**.
- **Template 2:** The LLM evaluates the same question again, but this time the roles of the **response** and the **reference** are swapped.

This dual-perspective approach guarantees a fair assessment of the answer's accuracy.

**Step 2:** If both ratings are valid, the final score is average of the score1 and score2 otherwise, it takes the valid one.

**Example Calculation:**

- **User Input:** "When was Einstein born?"
- **Response:** "Albert Einstein was born in 1879."
- **Reference:** "Albert Einstein was born in 1879."

Assuming both templates return a rating of **4** (indicating an exact match), the conversion is as follows:

- A rating of **4** corresponds to **1** on the [0,1] scale.
- Averaging the two scores: (1 + 1) / 2 = **1**.

Thus, the final **Answer Accuracy** score is **1**.

### Similar Ragas Metrics

#### Answer Correctness
This metric gauges the accuracy of the generated answer compared to the ground truth by considering both semantic and factual similarity.

##### How it's calculated

**Step 1:** Decompose both the response and the reference into standalone statements. Each statement should represent a claim that can be independently verified.

**Step 2:** Analyze all response statements based on the reference and classify them as follows:
- **TP (True Positive):** Statements in the answer that are directly supported by one or more statements in the ground truth.
- **FP (False Positive):** Statements present in the answer but not directly supported by any statement in the ground truth.
- **FN (False Negative):** Statements found in the ground truth but missing from the answer.

**Step 3:** Calculate the F-beta score. This score is a weighted harmonic mean of precision and recall, taking into account TP, FP, FN, and a beta parameter that adjusts the emphasis on recall versus precision.

$$
\text{F}_\beta = \frac{(1+\beta^2) \times \text{Precision} \times \text{Recall}}{(\beta^2 \times \text{Precision}) + \text{Recall}}
$$

where

$$
\text{Precision} = \frac{TP}{TP + FP} \quad \text{and} \quad \text{Recall} = \frac{TP}{TP + FN}.
$$

**Step 4:** Compute the semantic similarity between the reference and the response.

**Step 5:** Derive the final Answer Correctness score as the weighted average of the F-beta score and the semantic similarity score.


```python
from ragas.metrics import AnswerCorrectness, AnswerSimilarity

sample = SingleTurnSample(
    user_input="When was Einstein born?",
    response="Albert Einstein was born in 1879.",
    reference="Albert Einstein was born in 1879.",
)

scorer = AnswerCorrectness(
    llm=evaluator_llm,
    answer_similarity=AnswerSimilarity(embeddings=evaluator_embeddings),
)  # evaluator_llm wrapped with ragas LLM Wrapper

score = await scorer.single_turn_ascore(sample)
print(score)
```

    0.9999998164097105


#### Answer Correctness vs. Answer Accuracy

- **LLM Calls:** Answer Correctness requires three LLM calls (two for decomposing the response and reference into standalone statements and one for classifying them), while Answer Accuracy uses two independent LLM judgments.
- **Token Usage:** Answer Correctness consumes lot more tokens due to its detailed breakdown and classification process.
- **Explainability:** Answer Correctness offers high explainability by providing detailed insights into factual correctness and semantic similarity, whereas Answer Accuracy provides a straightforward raw score.
- **Robust Evaluation:** Answer Accuracy ensures consistency through dual LLM evaluations, while Answer Correctness offers a holistic view by deeply assessing the quality of the response.

#### **Rubric Score**

Rubric Score is a general-purpose metric that evaluates responses based on user-defined criteria and can be adapted to assess **Answer Accuracy** by aligning the rubric with the reference answer requirements.  

In this approach, the LLM reviews the provided rubric along with the response and the reference, then assigns a score and detailed explanation that outlines how well the response meets the specified criteria, reflecting how closely it adheres to the desired answer accuracy.


```python
from ragas.dataset_schema import SingleTurnSample
from ragas.metrics import RubricsScore

sample = SingleTurnSample(
    user_input="When was Einstein born?",
    response="Albert Einstein was born in 1879.",
    reference="Albert Einstein was born in 1879."
)

rubrics = {
    "score0_description": "If response is not contained in reference or not accurate in all terms, topics, numbers, metrics, dates and units or the response do not answer the user_input.",
    "score0.5_description": "If response is partially contained and almost equivalent to reference in all terms, topics, numbers, metrics, dates and units.",
    "score1_description": "If response is full contained and equivalent to reference in all terms, topics, numbers, metrics, dates and units.",
}

scorer = RubricsScore(rubrics=rubrics, llm=evaluator_llm) # evaluator_llm wrapped with ragas LLM Wrapper
await scorer.single_turn_ascore(sample)
```




    1



#### Answer Accuracy vs. Rubric Score  

- **LLM Calls**: Answer Accuracy makes two calls (one per LLM judge), while Rubric Score requires only one.
- **Token Usage**: Answer Accuracy is minimal since it outputs just a score, whereas Rubric Score generates reasoning, increasing token consumption.
- **Explainability**: Answer Accuracy provides a raw score without justification, while Rubric Score offers reasoning with verdict.
- **Efficiency**: Answer Accuracy is lightweight and works very well with smaller models.

# Context Relevance

**Context Relevance** evaluates whether the **retrieved_contexts** (chunks or passages) are pertinent to the **user_input**. This is done via two independent "LLM-as-a-judge" prompt calls that each rate the relevance on a scale of **0, 1, or 2**. The ratings are then converted to a [0,1] scale and averaged to produce the final score. Higher scores indicate that the contexts are more closely aligned with the user's query.

- **0** → The retrieved contexts are not relevant to the user’s query at all.
- **1** → The contexts are partially relevant.
- **2** → The contexts are fully relevant.


```python
from ragas.dataset_schema import SingleTurnSample
from ragas.metrics._nv_metrics import ContextRelevance

sample = SingleTurnSample(
    user_input="When and Where Albert Einstein was born?",
    retrieved_contexts=[
        "Albert Einstein was born March 14, 1879.",
        "Albert Einstein was born at Ulm, in Württemberg, Germany.",
    ]
)

scorer = ContextRelevance(llm=evaluator_llm)
score = await scorer.single_turn_ascore(sample)
print(score)
```

    1.0


### How It’s Calculated

**Step 1:** The LLM is prompted with two distinct templates (template_relevance1 and template_relevance2) to evaluate the relevance of the retrieved contexts with respect to the user's query. Each prompt returns a relevance rating of **0**, **1**, or **2**.

**Step 2:** Each rating is normalized to a [0,1] scale by dividing by 2. If both ratings are valid, the final score is the average of these normalized values; if only one is valid, that score is used.

**Example Calculation:**

- **User Input:** "When and Where Albert Einstein was born?"
- **Retrieved Contexts:**
  - "Albert Einstein was born March 14, 1879."
  - "Albert Einstein was born at Ulm, in Württemberg, Germany."

In this example, the two retrieved contexts together fully address the user's query by providing both the birth date and location of Albert Einstein. Consequently, both prompts would rate the combined contexts as **2** (fully relevant). Normalizing each score yields **1.0** (2/2), and averaging the two results maintains the final Context Relevance score at **1**.

### Similar Ragas Metrics

#### Context Precision
Context Precision measures the proportion of retrieved contexts that are relevant to answering a user's query. It is computed as the mean precision@k across all retrieved chunks, indicating how accurately the retrieval system ranks relevant information.

##### How it's calculated

**Step 1:** For each chunk in the retrieved contexts, determine its relevance to the user query by comparing it against the response or reference, resulting in a binary relevance indicator (0 for not relevant, 1 for relevant).

**Step 2:** For each rank \( k \) in the list of retrieved contexts, calculate Precision@\( k \) as the ratio of the number of relevant chunks up to that rank to the total number of chunks considered at that rank.

**Step 3:** Derive the final Context Precision score by averaging the Precision@\( k \) values across all chunks, yielding a score between 0 and 1.


```python
from ragas.dataset_schema import SingleTurnSample
from ragas.metrics import ContextPrecision

sample = SingleTurnSample(
    user_input="When and Where Albert Einstein was born?",
    retrieved_contexts=[
        "Albert Einstein was born March 14, 1879.",
        "Albert Einstein was born at Ulm, in Württemberg, Germany.",
    ],
    reference="14 March 1879, Ulm, Germany",
)

scorer = ContextRelevance(llm=evaluator_llm)
score = await scorer.single_turn_ascore(sample)
print(score)
```

    1.0


#### Context Recall

Context Recall quantifies the extent to which the relevant information is successfully retrieved. It is calculated as the ratio of the number of relevant claims (or contexts) found in the retrieved results to the total number of relevant claims in the reference, ensuring that important information is not missed.

##### How it's calculated


**Step 1:** Decompose the reference answer (or reference contexts) into standalone, verifiable claims.

**Step 2:** For each claim, evaluate whether it is supported by the retrieved contexts.

**Step 3:** Compute the Context Recall score as the ratio of the number of claims supported by the retrieved contexts to the total number of claims in the reference, resulting in a score between 0 and 1.


```python
from ragas.dataset_schema import SingleTurnSample
from ragas.metrics import ContextRecall

sample = SingleTurnSample(
    user_input="When and Where Albert Einstein was born?",
    retrieved_contexts=[
        "Albert Einstein was born March 14, 1879.",
        "Albert Einstein was born at Ulm, in Württemberg, Germany.",
    ],
    reference="14 March 1879, Ulm, Germany",
)

scorer = ContextRelevance(llm=evaluator_llm)
score = await scorer.single_turn_ascore(sample)
print(score)
```

    1.0


#### Context Precision and Context Recall vs. Context Relevance

- **LLM Calls:** Context Precision and Context Recall each require one LLM call each, one verifies context usefulness to get reference (verdict "1" or "0") and one classifies each answer sentence as attributable (binary 'Yes' (1) or 'No' (0)) while Context Relevance uses two LLM calls for added robustness.
- **Token Usage:** Context Precision and Context Recall consume lot more tokens, whereas Context Relevance is more token-efficient.
- **Explainability:** Context Precision and Context Recall offer high explainability with detailed reasoning, while Context Relevance provides a raw score without explanations.
- **Robust Evaluation:** Context Relevance delivers a more robust evaluation through dual LLM judgments compared to the single-call approach of Context Precision and Context Recall.

#### Rubric Score
Additionally, the Rubric Score can be adapted to measure context relevance. Similar to what we have done in Answer Accuracy:


```python
from ragas.dataset_schema import SingleTurnSample
from ragas.metrics import RubricsScore

sample = SingleTurnSample(
    user_input="When and Where Albert Einstein was born?",
    retrieved_contexts=[
        "Albert Einstein was born March 14, 1879.",
        "Albert Einstein was born at Ulm, in Württemberg, Germany.",
    ]
)

rubrics = {
    "score0_description": (
        "The Context provides no relevant information—either the response is absent or inaccurate in all aspects (topics, numbers, metrics, dates, or units) or fails to address the user_input."
    ),
    "score0.5_description": (
        "The Context provides partial information—the response is nearly equivalent to the Reference but has minor omissions or discrepancies in topics, numbers, metrics, dates, or units."
    ),
    "score1_description": (
        "The Context provides complete information—the response fully matches the Reference in every aspect, including topics, numbers, metrics, dates, and units."
    ),
}


scorer = RubricsScore(rubrics=rubrics, llm=evaluator_llm) # evaluator_llm wrapped with ragas LLM Wrapper
await scorer.single_turn_ascore(sample)
```




    1



# Response Groundedness

**Response Groundedness** measures how well a response is supported or "grounded" by the retrieved contexts. It assesses whether each claim in the response can be found, either wholly or partially, in the provided contexts.

- **0** → The response is **not** grounded in the context at all.
- **1** → The response is partially grounded.
- **2** → The response is fully grounded (every statement can be found or inferred from the retrieved context).


```python
from ragas.dataset_schema import SingleTurnSample
from ragas.metrics import ResponseGroundedness

sample = SingleTurnSample(
    response="Albert Einstein was born in 1879.",
    retrieved_contexts=[
        "Albert Einstein was born March 14, 1879.",
        "Albert Einstein was born at Ulm, in Württemberg, Germany.",
    ]
)

scorer = ResponseGroundedness(llm=evaluator_llm)
score = await scorer.single_turn_ascore(sample)
print(score)
```

    1.0


### How It’s Calculated

**Step 1:** The LLM is prompted with two distinct templates to evaluate the grounding of the response with respect to the retrieved contexts. Each prompt returns a grounding rating of **0**, **1**, or **2**.

**Step 2:** Each rating is normalized to a [0,1] scale by dividing by 2 (i.e., 0 becomes 0.0, 1 becomes 0.5, and 2 becomes 1.0). If both ratings are valid, the final score is computed as the average of these normalized values; if only one is valid, that score is used.

**Example Calculation:**

- **Response:** "Albert Einstein was born in 1879."
- **Retrieved Contexts:**
  - "Albert Einstein was born March 14, 1879."
  - "Albert Einstein was born at Ulm, in Württemberg, Germany."

In this example, the retrieved contexts provide both the birth date and location of Albert Einstein. Since the response's claim is supported by the context (even though the date is partially provided), both prompts would likely rate the grounding as **2** (fully grounded). Normalizing a score of 2 gives **1.0** (2/2), and averaging the two normalized ratings maintains the final Response Groundedness score at **1**.

### Similar Ragas Metrics

#### Faithfulness

This metric measures how factually consistent a response is with the retrieved context, ensuring that every claim in the response is supported by the provided information. The Faithfulness score ranges from 0 to 1, with higher scores indicating better consistency.

##### How it's calculated

**Step 1:** Identify all the claims in the response. Each claim should represent an assertion that can be independently verified using the retrieved context.

**Step 2:** For each claim, check whether it can be inferred or directly supported by the retrieved context.

**Step 3:** Compute the Faithfulness Score using the following formula:

$$
\text{Faithfulness Score} = \frac{\text{Number of claims in the response supported by the retrieved context}}{\text{Total number of claims in the response}}
$$

A response is considered fully faithful if all its claims are supported by the retrieved context (score = 1). If none of the claims are supported, the score will be 0.


```python
from ragas.dataset_schema import SingleTurnSample
from ragas.metrics import Faithfulness

sample = SingleTurnSample(
    user_input="When was Einstein born?",
    response="Albert Einstein was born in 1879.",
    retrieved_contexts=[
        "Albert Einstein was born March 14, 1879.",
        "Albert Einstein was born at Ulm, in Württemberg, Germany.",
    ]
)

scorer = Faithfulness(llm=evaluator_llm)
score = await scorer.single_turn_ascore(sample)
print(score)
```

    1.0


#### Faithfulness vs. Response Groundedness

- **LLM Calls:** Faithfulness requires two calls for detailed claim breakdown and verdict, while Response Groundedness uses two independent LLM judgments.
- **Token Usage:** Faithfulness consumes more tokens, whereas Response Groundedness is more token-efficient.
- **Explainability:** Faithfulness provides transparent, reasoning for each claim, while Response Groundedness delivers a raw score.
- **Robust Evaluation:** Faithfulness incorporates user input for a comprehensive assessment, whereas Response Groundedness ensures consistency through dual LLM evaluations.

#### Rubric Score

Additionally, the **Rubric Score** can be adapted to measure Response Groundedness (or Faithfulness) by providing a custom rubric. This approach allows evaluators to tailor the scoring criteria to assess whether the response is fully supported by the retrieved context.


```python
from ragas.dataset_schema import SingleTurnSample
from ragas.metrics import RubricsScore

sample = SingleTurnSample(
    user_input="When and Where Albert Einstein was born?",
    retrieved_contexts=[
        "Albert Einstein was born March 14, 1879.",
        "Albert Einstein was born at Ulm, in Württemberg, Germany.",
    ]
)

rubrics = {
    "score0_description": (
        "No support: the context or assertion is empty, or the assertion is not supported by the context."
    ),
    "score0.5_description": (
        "Partial support: the assertion is only partially supported by the context."
    ),
    "score1_description": (
        "Full support: the assertion is completely supported by the context."
    ),
}

scorer = RubricsScore(rubrics=rubrics, llm=evaluator_llm) # evaluator_llm wrapped with ragas LLM Wrapper
await scorer.single_turn_ascore(sample)
```




    1


