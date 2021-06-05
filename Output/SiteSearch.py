"""
This File contains functions for pulling information from sites and wrappers for site functions
"""

from .IPAddress import *
from .PhoneNumber import *
from ..API.Responses import *


class SearchEngine:
    def __init__(self, queryType:str, data:list or str):
        self.queryType = queryType
        self.data = data
        self.response = {}

    def searchType(self):
        """
        sets self.responses to be the results of all searches of type self.searchType
        :return: ResponseType object
        """
        if self.queryType == "IP":
            self.response = searchIp(self.data[1])
        if self.queryType == "PHONE":
            self.response = searchPhoneNumber(self.data)
        if self.queryType == "USERNAME":
            self.response = {}

    def generateResponse(self, query:str) -> IpResponse or PhoneResponse or Response:
        """
        uses self.responses to create the relevant response Object type
        :return: the response object
        """
        try:
            self.searchType()
            if self.queryType == "IP":
                return IpResponse(query, self.response)
            if self.queryType == "PHONE":
                return PhoneResponse(query, self.response)
            if self.queryType == "USERNAME":
                return Response(query)
        except ValueError:
            return NoResponse(query, self.queryType)
