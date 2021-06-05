from .API import Response
import re
from typing import Dict

EMAIL_SITES = []
IP_SITES = []
PHONE_SITES = []


class ErrorResponse(Response):
    def __init__(self, query: str, error: Exception):
        super().__init__(query)
        self.exception = re.split("'", str(error.__class__))[1]
        self.message = error.__str__()


class NoResponse(Response):
    def __init__(self, query: str, queryType: str):
        super().__init__(query)
        self.queryType = queryType
        self.siteList = []
        self.setSites()

    def setSites(self) -> None:
        if self.queryType == "EMAIL":
            self.siteList = EMAIL_SITES

        elif self.queryType == "IP":
            self.siteList = IP_SITES

        elif self.queryType == "PHONE":
            self.siteList = PHONE_SITES


class PhoneResponse(Response):
    def __init__(self, query: str, dictInfo: Dict[str, str]):
        super().__init__(query)
        self.name = dictInfo["Name"]
        self.address = dictInfo["Address"]


class IpResponse(Response):
    def __init__(self, query: str, info_dict: Dict[str, str]):
        super().__init__(query)
        self.hostname = info_dict["hostname"]
        self.city = info_dict["city"]
        self.region = info_dict["region"]
        self.loc = info_dict["loc"]
        self.isp = info_dict["isp"]
        self.org = info_dict["org"]
        self.as_ = info_dict["as"]
