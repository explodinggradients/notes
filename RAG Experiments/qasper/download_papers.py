from __future__ import annotations
import typing as t
import logging
import os
from datasets import DatasetDict
from concurrent.futures import ThreadPoolExecutor, as_completed

from tqdm import tqdm
import arxiv

if t.TYPE_CHECKING:
    ...

logger = logging.getLogger(__name__)


def download_paper(paper_id: str, download_dir: str = "./data"):
    filename = f"{paper_id}.pdf"
    # check if file already exists
    if os.path.exists(os.path.join(download_dir, filename)):
        logger.info("File %s already exists. Skipping download.", filename)
    else:
        search = arxiv.Search(id_list=[paper_id])
        paper = next(arxiv.Client().results(search))
        paper.download_pdf(dirpath=download_dir, filename=filename)


def download_papers(ds: DatasetDict):
    train_ids, test_ids, val_ids = (
        set(ds["train"]["id"]),
        set(ds["test"]["id"]),
        set(ds["validation"]["id"]),
    )

    # Select which papers to download
    # paper_ids = list(train_ids.union(test_ids).union(val_ids))
    paper_ids = ds["validation"]["id"][:10]

    # Using ThreadPoolExecutor to download papers in parallel
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Submit all tasks and create a list to track them
        futures = {
            executor.submit(download_paper, paper_id): paper_id
            for paper_id in paper_ids
        }

        # Use tqdm to create a progress bar for the futures as they complete
        for future in tqdm(
            as_completed(futures), total=len(paper_ids), desc="Downloading Papers"
        ):
            paper_id = futures[future]
            try:
                # Attempt to get the result, which will block until the future is done
                future.result()
            except Exception as exc:
                print(f"{paper_id} generated an exception: {exc}")


if __name__ == "__main__":
    from datasets import load_dataset

    qasper_dataset = load_dataset("allenai/qasper")
    download_papers(t.cast(DatasetDict, qasper_dataset))
