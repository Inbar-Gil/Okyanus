import re
from API.API import QueryType


class EMail(QueryType):

    def isQueryType(self):
        """
            Checks if the EMail type Object's query property matches the general format of an email

            If the query matches fully, the Object's state property is changed to True.

            If the query matches the general format at first, but doesn't match the  prefix format,
            a ValueError is raised with a fitting message

            If the query doesn't match the general format at all, nothing happens (the Object's
            state property stays as False, because it was initialized as such).

            :return: None
        """
        if re.match(r'[a-zA-Z0-9._-]+@[\w.-]+', self.query):
            count = 0
            atSignIndex = self.query.find("@")
            prefix = self.query[0:atSignIndex]
            for char in prefix:
                if char == "." or char == "_" or char == "-":
                    count += 1
                else:
                    count = 0
                if count == 2:
                    raise ValueError("This email is not legal")
            self.state = True

    def formatQuery(self):
        """
            Used after function "isQueryType".

            Formats the EMail type Object's query property according to proper email formatting and
            puts the result in Object's data property ([PREFIX, DOMAIN, ENDING]).

            :return: None
        """
        atSignIndex = self.query.find("@")
        afterAtSignIndex = self.query[atSignIndex:]
        periodSignIndex = afterAtSignIndex.find(".")
        PREFIX = self.query[0:atSignIndex]
        DOMAIN = afterAtSignIndex[1:periodSignIndex]
        ENDING = afterAtSignIndex[periodSignIndex:]
        self.data = [PREFIX, DOMAIN, ENDING]
