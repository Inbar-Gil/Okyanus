import re

#string that will check
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

#function to return regex
def check(Ip):
    if (re.search(regex, Ip)):
        print("Valid Ip address")

    else :
        print("Invalid Ip address")


ip_input = input("Enter ip addres you want to check: ")
check(ip_input)