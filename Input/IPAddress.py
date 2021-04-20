import re

# string that will check
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"


# todo change var name in global standard (all capital letters) to REGEX_IP
# todo add explanation comment for RegEx or make it more understandable

# function to return regex
def check(Ip):  # todo change function name to fit API (isQueryIPAddress)
    if (re.search(regex, Ip)):
        print("Valid Ip address")  # todo instead of prints make return values true or false

    else:
        print("Invalid Ip address")

# todo add function for analyzing IPv4 or IPv6


if __name__ == "__main__":
    # todo add more comprehensive tests to check special cases for IP's
    ip_input = input("Enter ip addres you want to check: ")
    check(ip_input)
