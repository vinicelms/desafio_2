"""Script para salvar conteúdo em CSV"""

import csv
import datetime

class CsvWriter():

    def write_file(self, json_content):
        now = datetime.datetime.now()
        date = datetime.datetime.strftime(now, "%Y-%m-%d")

        headers = self.__get_headers(content=json_content)

        with open("the_guardian_api_results_{}.csv".format(date), "w") as csvfile:
            file = csv.writer(csvfile)
            file.writerow(headers)

            for result in json_content:
                line = []
                
                for header in headers:
                    line.append(result[header])
                
                file.writerow(line)

    def __get_headers(self, content):
        list_headers = []

        for header in content[0].keys():
            list_headers.append(header)

        list_headers.sort()

        return list_headers