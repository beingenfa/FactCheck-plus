import logging
import re

from langchain.text_splitter import RecursiveCharacterTextSplitter


class DataProcessor:
    """
    - [x] Load JSON Files: Read and parse JSON files to extract necessary information.
    - [x] Extract and Structure Data: Isolate key components such as the claim, verdict, and sources.
    - [x] Text Preprocessing: Clean and normalize text data to ensure consistency.
    - [x] Document Chunking: Split lengthy texts into manageable chunks suitable for embedding.
    - [ ] Embedding Generation: Convert text chunks into vector embeddings using a language model.
    - [ ] Storage Preparation: Organize embeddings and metadata for insertion into a vector database.
        """
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter()

    def process_data(self, data):
        claim = data["claim"]
        politifact_verdict = data["politifact_claim check"]
        sources = self.get_sources(data)
        logging.info(f"{claim} - {politifact_verdict} - {len(sources)} source articles")
        processed_sources = self.prepare_chunks_with_metadata(sources)

        return claim, politifact_verdict, processed_sources


    def get_sources(self,data):
        def filter_sources_to_those_with_text(sources):
            filtered_sources = []
            for source in sources:
                if "text" in source.keys():
                    if source["text"]:
                        filtered_sources.append(source)
            return filtered_sources

        filtered_politifact_sources = filter_sources_to_those_with_text(data["politifact sources"])
        logging.info(
            f"{len(filtered_politifact_sources)} out of {len(data["politifact sources"])} politifact sources to be used.")
        filtered_general_news_sources = filter_sources_to_those_with_text(data["news sources"])
        logging.info(
            f"{len(filtered_general_news_sources)} out of {len(data["news sources"])} general news sources to be used.")
        return filtered_politifact_sources + filtered_general_news_sources

    @staticmethod
    def clean_text(text):
        """
        Cleans the provided text by normalizing whitespace and removing unwanted characters.
        """
        text = re.sub(r'\s+', ' ', text)  # replace multiple whitespace/newlines with single space
        text = text.strip()  # remove leading/trailing whitespace
        return text

    def prepare_chunks_with_metadata(self, sources):
        """
        Split sources into chunks, attaching metadata to each chunk.
        """
        chunk_metadata = []

        for source in sources:
            cleaned_text = self.clean_text(source["text"])
            chunks = self.text_splitter.split_text(cleaned_text)
            del source["text"]

            for chunk in chunks:
                chunk_metadata.append({"text": chunk, "metadata": source})

        logging.info(f"Prepared {len(chunk_metadata)} chunks with metadata.")
        return chunk_metadata

