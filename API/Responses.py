import re
from typing import Dict

from .API import Response

IP_SITES = ["https://ipinfo.io/",
            "https://ipdata.co/?ref=iplocation",
            "https://censys.io/ipv4",
            "https://ip-api.com/",
            "https://www.threatcrowd.org/"]
EMAIL_SITES = ["https://centralops.net/co/emaildossier.aspx",
               "https://haveibeenpwned.com/",
               "https://tools.epieos.com/email.php"]
PHONE_SITES = ["https://www.truecaller.com/",
               "https://synapsint.com/",
               "https://441il.com/reverse_lookup/phone_number/israel.html",
               "https://imei24.com/",
               "https://intelx.io/tools?tab=telephone"]
USERNAME_SITES = ["https://knowem.com/",
                  "https://whatsmyname.app/",
                  "https://www.yooying.com/",
                  "https://foller.me/"]
DOMAIN_SITES = ["https://whois.domaintools.com/",
                "https://crt.sh/?q=",
                "https://www.similarweb.com/",
                "https://omail.io/leads/"]
INSTAGRAM_SITES = ["https://www.yooying.com/",
                   "https://www.searchmy.bio/",
                   "https://searchusers.com/",
                   "https://imginn.com/"]


class ErrorResponse(Response):
    def __init__(self, query: str, error: Exception):
        super().__init__(query)
        self.data = {"exception": re.split("'", str(error.__class__))[1],
                     "message": error.__str__()}
        self.dataKeys = list(self.data.keys())


class NoResponse(Response):
    def __init__(self, query: str, queryType: str):
        super().__init__(query)
        self.queryType = queryType
        self.data = {"queryType": queryType}
        self.dataKeys = list(self.data.keys())
        self.setSites()

    def setSites(self) -> None:
        if self.queryType == "EMAIL":
            self.links = EMAIL_SITES

        elif self.queryType == "IP":
            self.links = IP_SITES

        elif self.queryType == "PHONE":
            self.links = PHONE_SITES

        elif self.queryType == "USERNAME":
            self.links = USERNAME_SITES


class PhoneResponse(Response):
    def __init__(self, query: str, dictInfo: Dict[str, str]):
        super().__init__(query)
        self.links = PHONE_SITES
        self.data = dictInfo
        self.dataKeys = list(self.data.keys())


class IpResponse(Response):
    def __init__(self, query: str, info_dict: Dict[str, str]):
        super().__init__(query)
        self.links = IP_SITES
        self.data = info_dict
        self.dataKeys = list(self.data.keys())
