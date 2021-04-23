"""
This File contains functions for pulling information from sites and wrappers for site functions
"""

from Output.EMail import *
from Output.IPAddress import *
from Output.PhoneNumber import *


class SearchEngine:
    def __init__(self, queryType, data):
        self.searchType = queryType
        self.data = data
        self.response = ""

    def searchType(self):
        """
        sets self.responses to be the results of all searches of type self.searchType
        :return:
        """
        pass

    def generateResponse(self, query):
        """
        uses self.responses to create the relevant response Object type
        :return: the response object
        """
        self.searchType()
        return self.response
