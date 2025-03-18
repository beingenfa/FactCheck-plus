from src.core.data_aggregator.DataAggregator import DataAggregator
from src.core.data_processor.DataProcessor import DataProcessor
from src.utils.data_io import read_json


class Pipeline:
    def __init__(self):
        self.data_aggregator = DataAggregator()
        self.data_processor = DataProcessor()

    def generate_report_for_politifact_claim_url(self,source, source_type):
        data = None
        assert source_type in ['url','file']
        if source_type == 'url':
            data = self.data_aggregator.extract_claim_related_data_given_politifact_url(politifact_url=source)
        elif source_type == 'file':
            data = read_json(source)
        if data:
            claim, politifact_verdict, processed_sources = self.data_processor.process_data(data)
        return True