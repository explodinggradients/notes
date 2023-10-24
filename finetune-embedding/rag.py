
from llama_index import SimpleDirectoryReader, VectorStoreIndex, ServiceContext, StorageContext
from llama_index.node_parser import SimpleNodeParser
from llama_index.text_splitter import TokenTextSplitter
from llama_index.storage.docstore import SimpleDocumentStore
from llama_index.storage.index_store import SimpleIndexStore
from llama_index.vector_stores import SimpleVectorStore

from transformers import AutoTokenizer
from langchain.embeddings import HuggingFaceEmbeddings
from datasets import Dataset, concatenate_datasets
import os
import json
from ragas.metrics.context_precision import ContextPrecision
import re
import numpy as np
import argparse
from preprocess import load_dataset
from tqdm import tqdm

# os.environ['OPENAI_API_KEY'] = json.load(open("/home/shahul/openai-keys.json"))["ikka"]

context_precision = ContextPrecision()


def get_files_to_load(dataset, data_dir, add_noise=200):
    files = set([re.sub(r'#.*','',url.split('/')[-1]) for url in dataset["Answer_URL"] if 'wikipedia' in url])
    files = [f"{file}.txt" for file in files]
    
    if add_noise:
        noise_files = os.listdir(data_dir)
        files.extend(np.random.choice(noise_files, add_noise).tolist())
        
    return files


def read_docs(datadir, files):
    input_files = [os.path.join(datadir, file) for file in files if os.path.exists(os.path.join(datadir, file))]
    reader = SimpleDirectoryReader(input_files=input_files)
    data = reader.load_data()
    return data


def prepare_tokenizer(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name,trucation_side='left')
    tokenizer.truncation_side = "left"
    tokenizer.model_max_length = 512
    return tokenizer


def prepare_node_parser(tokenizer, chunk_size):
    
    token_splitter = TokenTextSplitter(chunk_size=chunk_size
                                       , chunk_overlap=chunk_size//10, tokenizer=tokenizer.encode)
    node_parser = SimpleNodeParser.from_defaults(text_splitter=token_splitter)
    return node_parser


def get_retriver(dataset, datadir,tokenizer,embed_model, chunk_size, batch_id, top_k, add_noise):

    files = get_files_to_load(dataset, datadir, add_noise)
    docs = read_docs(datadir, files)
    node_parser = prepare_node_parser(tokenizer, chunk_size)

    
    # create storage context using default stores
    storage_context = StorageContext.from_defaults(
        docstore=SimpleDocumentStore(),
        vector_store=SimpleVectorStore(),
        index_store=SimpleIndexStore(),
    )

    service_context = ServiceContext.from_defaults(node_parser=node_parser, embed_model=embed_model, llm=None)
    index = VectorStoreIndex.from_documents(docs, storage_context=storage_context, service_context=service_context)     
    index.storage_context.persist(persist_dir=f"sample-{batch_id}.index")
    retreiver = index.as_retriever(similarity_top_k=top_k)

    return retreiver 

def prepare_query(item, tokenizer):
    context, question = item['Context'], item["Question"]
    query = "\n".join(context) + tokenizer.sep_token + question
    query = tokenizer.decode(tokenizer.encode(query,max_length=512,truncation=True, add_special_tokens=False))
    return query 
    
def get_ragas_score(dataset):
    
    dict = {"question":[item["Rewrite"] for item in dataset],
        "contexts":[[node["node"].get("text") for node in item["chunks"]] for item in dataset],}
    return context_precision.score(Dataset.from_dict(dict))

def main(batch_size,train_data,data_dir, model_name, output_dir,min_chunk_size, max_chunk_size,top_k,add_noise):
    
    subset = 'quac'
    dataset = load_dataset(train_data, subset).select(range(0,3501))
    tokenizer = prepare_tokenizer(model_name)
    model = HuggingFaceEmbeddings(model_name=model_name)
    chunk_size = np.random.randint(min_chunk_size, max_chunk_size)
    subsample_list = []
    for batch_id in range(0, len(dataset), batch_size):
        subsample = dataset.select(range(batch_id, min(len(dataset),batch_id+batch_size)))
        retreiver = get_retriver(subsample, data_dir, tokenizer, model, chunk_size, batch_id, top_k,add_noise)

        for item in tqdm(subsample):
            query = prepare_query(item, tokenizer)
            chunks = retreiver.retrieve(query)
            item.update({"chunks":[chunk.to_dict() for chunk in chunks]})
            subsample_list.append(item)
    
    ragas_scores = get_ragas_score(subsample_list)["context_precision"]
    _ = [item.update({"ragas_score":score}) for item, score in zip(subsample_list, ragas_scores)]
    with open(os.path.join(output_dir, "subset.json"),"w") as file:
        json.dump(subsample_list, file, indent=4)
        

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--train_data", type=str, help="Path of the train data", default="/home/shahul/data/qrecc-training.json")
    parser.add_argument("--data_dir", type=str, help="Path to wikidata",default="wikidata")
    parser.add_argument("--output_dir", type=str, help="Path to save index",default="./wikidata/indices")
    parser.add_argument("--model_name", type=str ,default="BAAI/bge-small-en-v1.5")

    parser.add_argument("--batch_size", type=int, default=100)
    parser.add_argument("--min_chunk_size", type=int, default=256)
    parser.add_argument("--max_chunk_size", type=int, default=512)
    parser.add_argument("--top_k", type=int, default=10)
    parser.add_argument("--add_noise", type=int, default=100)


    args = parser.parse_args().__dict__
    
    main(**args)



