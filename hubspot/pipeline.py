import json
from hubspot3.base import BaseClient


PIPELINES_API_VERSION = "1"


class PipelineClient(BaseClient):
    """
    Lets you extend to non-existing clients, this example extends pipelines
    """

    def __init__(self, *args, **kwargs):
        super(PipelineClient, self).__init__(*args, **kwargs)

    def _get_path(self, subpath):
        return "crm-pipelines/v{}/{}".format(
            self.options.get("version") or PIPELINES_API_VERSION, subpath
        )
    
    def get_pipelines(self, **options):
        params = {}
        return self._call(
            "pipelines/{}".format(
                options.get('object_type') or 'deals'
            ),
            method="GET", params=params
        )
    
    def get_all_pipelines(self):
        res = []
        for t in ['deals', 'tickets']:
            res.append(self.get_pipelines(object_type=t)['results'][0])
        return res