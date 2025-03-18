import re, os, uuid
from datetime import datetime
from src.utils.data_io import write_json

from src.core.data_aggregator.config.paths import content_root

from src.core.data_aggregator.NewsAggregator import NewsAggregator
from src.core.data_aggregator.PolitiFactScraper import PolitiFactScraper

class DataAggregator:
    def __init__(self):
        self.news_agg = NewsAggregator()
        self.politifact_scraper = PolitiFactScraper()

    def extract_claim_related_data_given_politifact_url(self, politifact_url,save = True):
        claim_id = uuid.uuid4().__str__()
        politifact_data = self.politifact_scraper.return_page_content(article_url=politifact_url)
        search_claim =  re.sub(r'[^A-Za-z0-9 ]+', '', politifact_data['claim'])
        news_agg = self.news_agg.fetch_news(search_claim)
        agg_data = {
            'claim': politifact_data['claim'],
            'politifact_claim check': politifact_data['claim check'],
            'politifact sources': politifact_data['sources'],
            'news sources': news_agg,
            '_meta': {
                'politoco': {
                    'page url': politifact_url,
                    'page content': politifact_data['content']
                },
            },
            '_internal_claim_id': claim_id,
            '_search query' : search_claim,
            '_data extracted date': datetime.now().__str__()

        }
        if save:
            write_json(data=agg_data,file_path=os.path.join(content_root + f"/claims/{claim_id}.json"))

        return agg_data