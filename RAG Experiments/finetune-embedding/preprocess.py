from datasets import Dataset
import wikipediaapi
import argparse
import os
from tqdm import tqdm
import re

wiki_wiki = wikipediaapi.Wikipedia(
        user_agent='MyProjectName (merlin@example.com)',
        language='en',
)


def load_dataset(path, subset):
    
    dataset = Dataset.from_json(path)
    return dataset.filter(lambda example: example["Conversation_source"]==subset)


def scrape_wiki(page):

   page = wiki_wiki.page(page)
   if page.exists():
       return page.text
   
   return None

def write_to_file(data, filepath):
    
    with open(filepath, 'w') as file:
        file.write(data)
    

def main(**args):
    
    dataset = load_dataset(args.get("filepath"), args.get("source"))
    pages = set([re.sub(r'#.*','',url.split('/')[-1]) for url in dataset["Answer_URL"] if 'wikipedia' in url])
    dirname = args.get("savepath")
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    
    for page in tqdm(pages):
        if page:
            try:
                text = scrape_wiki(page)
                filename = os.path.join(dirname, page+".txt")
                if text:
                    write_to_file(text, filename)
            except Exception as e:
                print(f"An exception occured at {page}")
                

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--filepath", type=str, help="Path of the data file")
    parser.add_argument("--savepath", type=str, help="Path to store data",default="wikidata")
    parser.add_argument("--source", type=str, help="Conversation source", default="quac")
    args = parser.parse_args().__dict__
    
    main(**args)
    