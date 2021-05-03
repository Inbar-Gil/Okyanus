from API.API import Response
import re


class ErrorResponse(Response):
    def __init__(self, query, error):
        super().__init__(query)
        self.exception = re.split("'", str(error.__class__))[1]
        self.message = error.__str__()
