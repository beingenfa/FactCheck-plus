import logging
from src.core.Pipeline import Pipeline
logging.basicConfig(level=logging.INFO)
pipeline_obj = Pipeline()
pipeline_obj.generate_report_for_politifact_claim_url(source="../../data/claims/2d9a9d81-4774-48a8-9f7a-07bb2610333d.json", source_type="file")