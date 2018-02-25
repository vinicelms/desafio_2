"""Script para consumir API do site de notícias The Guardian"""

import requests
import json

class Api_Consumer():

    def __init__(self, api_key):
        self.BASE_URL = "https://content.guardianapis.com"
        self.API_KEY = api_key

    def search_content(self, section, date_start=None, date_end=None, qtt_results=10, all_content=False):
        req = None

        request_headers = {
            "Accept" : "application/json"
        }

        parameters = {
            "api-key" : self.API_KEY,
            "section" : section,
            "page-size" : qtt_results
        }

        req = requests.get(url="{}/search".format(self.BASE_URL), headers=request_headers, params=parameters)
        ret = req.content.decode("utf-8")
        ret = json.loads(ret)