import time

from tqdm import tqdm

from src.core.data_aggregator.DataAggregator import DataAggregator

politifact_urls =[
    "https://www.politifact.com/factchecks/2025/mar/13/karoline-leavitt/karoline-leavitt-says-tariffs-are-a-tax-cut-econom/",
    "https://www.politifact.com/factchecks/2025/mar/14/alex-jones/infowars-reporter-jamie-white-who-was-fatally-shot/",
    "https://www.politifact.com/factchecks/2025/mar/03/cavalier-johnson/mps-does-indeed-have-a-larger-tax-levy-than-the-ci/",
    "https://www.politifact.com/factchecks/2025/feb/28/joel-kitchens/do-90-of-wisconsin-school-districts-ban-cellphones/",
    "https://www.politifact.com/factchecks/2025/mar/12/jd-vance/did-the-cost-of-buying-a-home-double-under-joe-bid/",
    "https://www.politifact.com/factchecks/2025/feb/04/ron-johnson/wis-sen-johnson-says-us-is-one-of-very-few-nations/",
    "https://www.politifact.com/factchecks/2025/mar/11/better-wisconsin-together/did-court-candidate-schimel-not-join-71-wisconsin/",
    "https://www.politifact.com/factchecks/2025/feb/25/patty-murray/are-republican-tax-cuts-the-single-biggest-driver/",
    "https://www.politifact.com/factchecks/2025/feb/26/kevin-oleary/kevin-oleary-shark-tanks-mr-wonderful-says-no-gove/",
    "https://www.politifact.com/factchecks/2025/feb/21/elon-musk/fact-check-elon-musk-cpac-bidens-immigration-polic/"
    ]

obj = DataAggregator()
for politifact_url in tqdm(politifact_urls,"Extracting data from politifact"):
    obj.extract_claim_related_data_given_politifact_url(politifact_url)
    time.sleep(2)
