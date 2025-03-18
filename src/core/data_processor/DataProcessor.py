import logging


class DataProcessor:
    """
    - [x] Load JSON Files: Read and parse JSON files to extract necessary information.
    - [x] Extract and Structure Data: Isolate key components such as the claim, verdict, and sources.
    - [ ] Text Preprocessing: Clean and normalize text data to ensure consistency.
    - [ ] Document Chunking: Split lengthy texts into manageable chunks suitable for embedding.
    - [ ] Embedding Generation: Convert text chunks into vector embeddings using a language model.
    - [ ] Storage Preparation: Organize embeddings and metadata for insertion into a vector database.
        """
    def __init__(self):
        pass

    def process_data(self, data):
        claim = data["claim"]
        politifact_verdict = data["politifact_claim check"]
        sources = self.get_sources(data)
        logging.info(f"{claim} - {politifact_verdict} - {len(sources)} source articles")
        print("")

    @staticmethod
    def get_sources(data):
        def filter_sources_to_those_with_text(data):
            filtered_sources = []
            for source in data:
                if "text" in source.keys():
                    if source["text"]:
                        filtered_sources.append(source)
            return filtered_sources

        filtered_politifact_sources = filter_sources_to_those_with_text(data["politifact sources"])
        logging.info(
            f"{len(filtered_politifact_sources)} out of {len(data['politifact sources'])} politifact sources to be used.")
        filtered_general_news_sources = filter_sources_to_those_with_text(data["news sources"])
        logging.info(
            f"{len(filtered_general_news_sources)} out of {len(data['news sources'])} general news sources to be used.")
        return filtered_politifact_sources + filtered_general_news_sources
