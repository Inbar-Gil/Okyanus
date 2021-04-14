"""
This File contains function structures for bot input and output modules
and naming conventions
"""


def isQueryType(query):
    """
    Is the query given of data type specified
    :param query: the query given for the search
    :return: True if it is the data type, False otherwise
    """
    pass


def formatQueryType(query):
    """
    After checking the query type, formats it to all relevant data portions
    :param query: the query of known typ
    :return: tuple of all the relevant data for each site
    """
    pass


def siteTypeSearch(data, *args):
    """
    Uses formatted data to automatically search a site
    :param data: the formatted data
    :param args: antyhing else needed to use the site (username etc.)
    :return: the search result as raw data
    """
    pass


class Response:
    """
    Class to use to format answers onto to use Django
    """

    def __init__(self, query):
        self.query = query
        self.answer = ""
