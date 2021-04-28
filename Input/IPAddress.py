import re

VALID_IP = False
# regex string for validating an Ip-address
REGEX_IP = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
# regex string for validating an its a ipv6
RE_IPV6 = "(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"


# function to return regex
def isQueryIPAddress(Ip):
    if re.search(REGEX_IP, Ip) or re.search(RE_IPV6, Ip):
        return True
    else:
        return False


def formatIPAddress(Ip):
    for i in range(0, len(Ip), 1):
        if "." in Ip:
            return "IPv4", Ip
        elif ":" in Ip:
            return "IPv6", Ip


if __name__ == '__main__':
    Ip = "254.1.2.2"
    print(isQueryIPAddress(Ip))
    print(formatIPAddress(Ip))
    Ip = "64ba:c4c9:60ee:1f20:e034:b8ab:49d2:ee2e"
    print(isQueryIPAddress(Ip))
    print(formatIPAddress(Ip))
    Ip = "6db8:1058:b70:63e0:f52c:39e:ac11:ab64"
    print(isQueryIPAddress(Ip))
    print(formatIPAddress(Ip))
