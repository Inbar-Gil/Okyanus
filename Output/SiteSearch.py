"""
This File contains functions for pulling information from sites and wrappers for site functions
"""

from Output.EMail import *
from Output.IPAddress import *
from Output.PhoneNumber import *
from API.API import *


class SearchEngine:
    def __init__(self, queryType, data):
        self.queryType = queryType
        self.data = data
        self.response = Response("")

    def searchType(self):
        """
        sets self.responses to be the results of all searches of type self.searchType
        :return: ReponseType object
        """
        pass

    def generateResponse(self, query):
        """
        uses self.responses to create the relevant response Object type
        :return: the response object
        """
        self.response = Response(query)
        self.searchType()
        return self.response
