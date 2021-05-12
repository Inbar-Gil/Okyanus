import re
from API.API import QueryType

VALID_IP = False
# regex string for validating an Ip-address
REGEX_IP = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$"
# regex string for validating an its a ipv6
RE_IPV6_GENERAL = r"((\w{1,4}:){7}\w{1,4})"
RE_IPV6 = r"(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|" \
          r"([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|" \
          r"([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|" \
          r"([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|" \
          r"([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|" \
          r"([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|" \
          r"[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|" \
          r":((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|" \
          r"::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|" \
          r"(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|" \
          r"([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|" \
          r"(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"


class IP(QueryType):

    def isQueryType(self):
        """
            Checks if the IP type Object's query property matches the format of an IPv4/IPv6.

            If yes, the Object's state property is changed to True.

            If the query doesn't match any format at all, nothing happens (the Object's state
            property stays as False, because it was initialized as such).

            :return: None
        """
        if re.match(REGEX_IP, self.query):
            octet = re.split(r'\.', self.query)
            for x in octet:
                if int(x) > 255 or int(x) < 0:
                    raise ValueError("This IPv4 address is illegal")
            self.state = True
        elif re.match(RE_IPV6_GENERAL, self.query):
            if not (re.match(RE_IPV6, self.query)):
                raise ValueError("This IPv6 address is illegal")
            self.state = True

    def formatQuery(self):
        """
            Used after function "isQueryType".

            Checks if the IP Object's query property is specifically an IPv4 or an IPv6 address.

            Puts the result in the Object's date property ([IP type, self.query]).

            :return: None
         """
        for i in range(0, len(self.query), 1):
            if "." in self.query:
                self.data = ["IPv4", self.query]
            elif ":" in self.query:
                self.data = ["IPv6", self.query]


if __name__ == '__main__':
    Ip = IP("246.1.2.2")
    print(Ip.getQueryData())

    Ip = IP("FFXF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF")
    print(Ip.getQueryData())

    Ip = IP("6db8:1058:b70:63e0:f52c:39e:ac11:ab64")
    print(Ip.getQueryData())
