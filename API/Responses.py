from .API import Response
import re

EMAIL_SITES = []
IP_SITES = []
PHONE_SITES = []


class ErrorResponse(Response):
    def __init__(self, query, error):
        super().__init__(query)
        self.exception = re.split("'", str(error.__class__))[1]
        self.message = error.__str__()
        self.responseType = "ErrorResponse"


class NoResponse(Response):
    def __init__(self, query, queryType):
        super().__init__(query)
        self.queryType = queryType
        self.siteList = []
        self.setSites()
        self.responseType = "NoResponse"

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


class IpResponse(Response):
    def __init__(self, query, info_dict):
        super().__init__(query)
        self.hostname = info_dict["hostname"]
        self.city = info_dict["city"]
        self.region = info_dict["region"]
        self.loc = info_dict["loc"]
        self.isp = info_dict["isp"]
        self.org = info_dict["org"]
        self.as_ = info_dict["as"]
