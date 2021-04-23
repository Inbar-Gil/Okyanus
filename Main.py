"""
This File contains the main code running the script and Server interface
"""
from Input.RegExAnalyzer import *
from Output.SiteSearch import *


def main(query):
    analyzer = RegExAnalyzer(query)
    queryType, data = analyzer.returnData()
    engine = SearchEngine(queryType, data)
    response = engine.generateResponse(query)
    # jsonResponse = response.__dict__()
    jsonResponse = {"a": query, "b": ""}
    return jsonResponse
