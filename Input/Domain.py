import re
from ..API.API import QueryType
from urllib.parse import urlparse

DOMAIN_REGX = r'http[s]?://'


def known_sites(domain):
    if domain == "facebook.com":
        return "Facebook"
    if domain == "instagram.com":
        return "Instagram"
    if domain == "twitter.com":
        return "Twitter"
    return ""


class Domain(QueryType):

    def isQueryType(self) -> None:
        if re.match(DOMAIN_REGX, self.query):
            self.state = True

    def formatQuery(self) -> None:
        domain = urlparse(self.query).netloc
        domain = domain.replace("www.", "")

        protocol_name = self.query.split(':')[0]

        requested_page = self.query.split('//')[1].split('/')[-1]

        sub_folders = self.query.split('//')[1].split('/')[1:-1]

        is_known = known_sites(domain)

        self.data = domain, is_known, protocol_name, requested_page, sub_folders,


if __name__ == '__main__':
    print(re.match(DOMAIN_REGX, "https://www.facebook.com/groups/1461656040797270/user/100005066730592/"))
