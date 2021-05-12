from API import Response
import re

EMAIL_SITES = []
IP_SITES = []
PHONE_SITES = []


class ErrorResponse(Response):
    def __init__(self, query, error):
        super().__init__(query)
        self.exception = re.split("'", str(error.__class__))[1]
        self.message = error.__str__()


class NoResponse(Response):
    def __init__(self, query, queryType):
        super().__init__(query)
        self.queryType = queryType
        self.siteList = []
        self.setSites()

    def setSites(self):
        if self.queryType == "EMAIL":
            self.siteList = EMAIL_SITES

        elif self.queryType == "IP":
            self.siteList = IP_SITES

        elif self.queryType == "PHONE":
            self.siteList = PHONE_SITES


class PhoneResponse(Response):
    def __init__(self, query, dictInfo):
        super().__init__(query)
        self.name = dictInfo["Name"]
        self.address = dictInfo["Address"]



#p1 = PhoneResponse("08-62723431", {'Name': 'קינסברונר עמנואל', 'Address': 'לייב יפה 21 באר שבע'})
#print(p1.__dict__)
