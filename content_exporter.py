# -*- coding: utf-8 -*-
"""Script para exportar os dados coletados da API"""

from core.api_consumer import ApiConsumer
from core.csv_writer import CsvWriter
import argparse

def export_content(section, api_key, date_start=None, date_end=None, qtt_results=None):
    api = ApiConsumer(api_key=api_key)
    writer = CsvWriter()

    ret = api.search_content(section=section, date_start=date_start, date_end=date_end, qtt_results=qtt_results)
    results = ret["response"]["results"]
    writer.write_file(json_content=results)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--key", help="Chave de acesso da API do The Guardian", required=True,
    action="store")
    parser.add_argument("--section", help="Informa a seção que será buscada", required=True,
    action="store")
    parser.add_argument("--start", help="Define a data de início de pesquisa. Formato: YYYY-MM-DD",
    action="store")
    parser.add_argument("--end", help="Define a data de término de pesquisa. Formato: YYYY-MM-DD",
    action="store")
    parser.add_argument("--resultados", help="Define a quantidade de retornos que será solicitado para API. Máximo: 200",
    action="store")

    args = parser.parse_args()

    export_content(section=args.section, api_key=args.key, date_start=args.start, date_end=args.end, qtt_results=args.resultados)