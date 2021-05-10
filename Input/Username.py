from API.API import QueryType
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
        else:
            raise ValueError("This username is illegal")

    def formatQuery(self):
        """
            Used after function "isQueryType".

            Function gets the Username type Object's index of the next character out of ['.',',','-','_']
            and, using the Object's query property, adds each segment of text between the specified charcaters to a list.

            At the end, the function adds each of the list's elements to the Object's data property

            :return: None
        """
        self.data = re.split(r'\.|,|-|_',self.query)






