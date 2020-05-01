from hubspot3 import Hubspot3
from .pipeline import PipelineClient


class API:
    def __init__(self, key):
        self.key = key
        self.client = Hubspot3(api_key=key)
        self.pipeline_client = PipelineClient(api_key=key)
    
    def get_all_companies(self):
        return self.client.companies.get_all()
    
    def get_all_contacts(self):
        return self.client.contacts.get_all()
    
    def get_all_pipelines(self):
        return self.pipeline_client.get_all_pipelines()
    