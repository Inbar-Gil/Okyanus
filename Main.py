"""
This File contains the main code running the script and Server interface
"""
from Input.RegExAnalyzer import *
from Output.SiteSearch import *
from API.Responses import *
import okyanus.manage
import sys


def main(query):
    try:
        raise ValueError("hello world")
        analyzer = RegExAnalyzer(query)
        queryType, data = analyzer.returnData()
        engine = SearchEngine(queryType, data)
        response = engine.generateResponse(query)
        jsonResponse = response.__dict__
        return jsonResponse
    except Exception as e:
        response = ErrorResponse(query, e)
        jsonResponse = response.__dict__
        return jsonResponse


if __name__ == "__main__":
    okyanus.manage.main()
