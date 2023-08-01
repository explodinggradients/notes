# Langchain Internals
> Langchain as a framework is just text permutation and network calls to LLM APIs. The real magic is the community
> exploring the boundaries of what you can do with LLMs and implementing them back into the project.
> The collective wisdom and creativity of the community is truly special.

This is my notes as I'm exploring the LlamaIndex codebase. If you're looking to contribute or interested in understanding more about how Langchain works under the hood I think this would be useful for you too 🙂. 

### Basics
1. [Prompts](./prompts.ipynb) - Prompts is langchain's abstraction over the strings you pass into models but it does have some tricks up its sleeve that help you when building Apps.
2. [LLMs](./llms-completion.ipynb) - Using the LLM abstraction and the fancy 
   stuff it allows us to do. Access to a wide range of LLM endpoints.
3. [LLMs: chat models](./llms-chat.ipynb) - Chat Models are becoming more common
   and is cheaper too. In this notebook we'll see what langchain offers in this
   regards
4. [Chains](./chains.ipynb) - soon!
5. [Evaluations - Basics](./evaluations.ipynb) - A quick look into how
   evaluations are done in langchain.

### Langsmith
**The companion (tool) I've been waiting for**
langsmith has been a game changer for me when I'm developing and debugging LLM
apps. 

1. [Langsmith Overview](./langsmith-intro.ipynb) - Exploring all the langsmith
   features available.
2. [QA evaluation with Langsmith](./qa_evaluations.ipynb) - Covers how to
   evaluate with langsmith. It pretty neat way to visualize the results.
3. [Evalution with Ragas]() - soon!


### QA Systems
Langchain allows you to connect your own documents too ie building a basic
"Retrival Augmented Generation (RAG)" pipeline

1. [Intro](./QA-intro.ipynb) - Overview of the main steps involved.
2. [QA Evaluation](./qa_evaluations.ipynb) - How to evaluate RAG pipelines with
   the available evaluation chains.
