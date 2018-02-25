"""Script para consumir API do site de notícias The Guardian"""

import requests
import json
import datetime

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

        if date_start:
            try:
                # Validando valores informados
                date_start = datetime.datetime.strptime(date_start, "%Y-%m-%d")
                parameters["from-date"] = datetime.datetime.strftime(date_start, "%Y-%m-%d")
            except ValueError as e:
                return "Error in date_start: {}".format(e)
        if date_end:
            try:
                # Validando valores informados
                date_end = datetime.datetime.strptime(date_end, "%Y-%m-%d")
                parameters["to-date"] = datetime.datetime.strftime(date_end, "%Y-%m-%d")
            except ValueError as e:
                return "Error in date_end: {}".format(e)

        req = requests.get(url="{}/search".format(self.BASE_URL), headers=request_headers, params=parameters)
        ret = req.content.decode("utf-8")
        ret = json.loads(ret)