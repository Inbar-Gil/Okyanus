from typing import Tuple


class QueryType:

    def __init__(self, query: str):
        self.query: str = query
        self.state: bool = False
        self.data: Tuple = ()

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

    def getQueryData(self) -> Tuple[bool, tuple]:
        self.isQueryType()
        if self.state:
            self.formatQuery()
        return self.state, self.data


class Site:
    def __init__(self, data: tuple):
        self.data: tuple = data
        self.response: dict = {}

    def searchSite(self) -> dict:
        """
        searches the relevant Site and gets the response
        :return: the site's response
        """
        pass


class Response:
    def __init__(self, query: str) -> None:
        self.query: str = query
        self.responseType: str = self.__class__.__name__
        self.links: list = []
        self.data: dict = {}
        self.dataKeys = list(self.data.keys())
