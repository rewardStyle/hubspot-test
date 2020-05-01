import os
import logging
import json
from hubspot import hubspot

class App:
    def __init__(self):
        self.config = {}
        for k in ['APP_NAME', 'APP_ID', 'CLIENT_ID', 'CLIENT_SECRET', 'API_KEY']:
            self.config[k] = os.getenv(k)
        self.api = hubspot.API(self.config['API_KEY'])
    
    def info(self):
        logging.info('APP_NAME={} APP_ID={}'.format(
            self.config['APP_NAME'], self.config['APP_ID'])
        )
    
    def test(self):
        return {
            'companies': self.api.get_all_companies(),
            'contacts': self.api.get_all_contacts(),
            'pipelines': self.api.get_all_pipelines()
        }


def main():
    logging.basicConfig(format='[%(asctime)s] %(message)s', level=logging.INFO)
    app = App()
    app.info()
    logging.info(json.dumps(app.test(), indent=4))