"""
This File contains function structures for bot input and output modules
and naming conventions
"""

from typing import Tuple


class QueryType:

    def __init__(self, query: str):
        self.query = query
        self.state = False
        self.data = []

    def isQueryType(self) -> None:
        """
        Is the query given of data type specified
        changes self.state to be true if query is of type and false otherwise
        :raises ValueError for Incorrect format of type
        """
        pass

    def formatQuery(self) -> None:
        """
        After checking the query type, formats it to all relevant data portions
        changes self.data to be the formatted data
        """
        pass

    def getQueryData(self) -> Tuple[bool, list]:
        self.isQueryType()
        if self.state:
            self.formatQuery()
        return self.state, self.data


class Site:
    def __init__(self, data: str):
        self.data = data
        self.response = ""

    def searchSite(self) -> None:
        """
        searches the relevant Site and gets the response
        :return: the site's response
        """


class Response:
    """
    Class to use to format answers for use in main
    """

    def __init__(self, query: str) -> None:
        """
        insert headers to init
        """
        self.query = query
        self.responseType = self.__class__.__name__
