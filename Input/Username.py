from API import QueryType
import re


class Username(QueryType):
    def isQueryType(self):
        """
            Checks if the Username type Object's query property is a legal username.

            The function does this by checking if it starts with letters and not numbers.
            If yes, the Object's state property is changed to True.
            Else, the function raises a ValueError with the message "ILLEGAL USERNAME"

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

        run = True
        index = 0
        formatted = []
        try:
           index = next(i for i, c in enumerate(self.query) if c in {'.', ',', '-', '_'})
        except StopIteration:
            run = False
        if index is not None and run:
            run = True
            curr_query = self.query[0:index]
            formatted.append(curr_query)
            rest_query = self.query[index+1:]
            try:
                index = next(i for i, c in enumerate(rest_query) if c in {'.', ',', '-', '_'})
            except StopIteration:
                run = False
            while index is not None and run:
                curr_query = rest_query[0:index]
                formatted.append(curr_query)
                rest_query = rest_query[index+1:]
                try:
                    index = next(i for i, c in enumerate(rest_query) if c in {'.', ',', '-', '_'})
                except StopIteration:
                    run = False
                    rest_query = rest_query[0:]
                    formatted.append(rest_query)
            for x in formatted:
                self.data.append(x)
        else:
            self.data = [self.query]


x = Username("yu,val.navon").getQueryData()
print (x)
