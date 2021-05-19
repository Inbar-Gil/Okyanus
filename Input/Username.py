from ..API.API import QueryType
import re


class Username(QueryType):
    def isQueryType(self):
        """
            Checks if the Username type Object's query property is a legal username.

            The function does this by checking if it starts with letters and not numbers.
            If yes, the Object's state property is changed to True.
            Else, the function raises a ValueError with the message "This username is illegal"

            :return: None
        """

        if re.match(r'([a-zA-Z]+)', self.query):
            self.state = True

    def formatQuery(self):
        """
            Used after function "isQueryType".

            The function, using the Username type Object's query property, makes a list containing
            all of the segments of the query split by the characters ['.',',','-','_'] and puts
            that in the Object's data property.

            :return: None
        """
        self.data = re.split(r'[.,\-_]', self.query)
