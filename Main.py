"""
This File contains the main code running the script and Server interface
"""
from .Input.RegExAnalyzer import *
from .Output.SiteSearch import *
from .okyanus import manage


def main(query):
    try:
        analyzer = RegExAnalyzer(query)
        analyzer.getQueryType()
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
    manage.main()
