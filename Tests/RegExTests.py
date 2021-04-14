"""
This File creates 1000 random strings for Regex separation tests
"""
import string
import numpy as np

DATA_TYPES = 3


def createPhoneNumber():
    """
    International Format - 0
    Israel Mobile - 1
    Israel Home - 2
    :return: Phone number of the above formats
    """
    format = np.random.randint(0, 3)
    print(format)
    if format == 0:
        # +AAA NNNNNNNNN
        areaCode = np.random.randint(0, 1000)
        numbers = [str(digit) for digit in np.random.randint(0, 10, 9)]
        return "+" + str(areaCode) + "".join(numbers)
    if format == 1:
        # 05A NNNNNNN
        areaCode = np.random.randint(0, 10)
        numbers = [str(digit) for digit in np.random.randint(0, 10, 7)]
        hyphen = np.random.randint(0, 2)
        return "05" + str(areaCode) + "-" * hyphen + "".join(numbers)
    if format == 2:
        # AA A* NNNNNNN
        areaCode = np.random.choice(["02", "03", "04", "08", "09", "077"])
        numbers = [str(digit) for digit in np.random.randint(0, 10, 7)]
        hyphen = np.random.randint(0, 2)
        return areaCode + "-" * hyphen + "".join(numbers)


def createIPAddress():
    # ddd.ddd.ddd.ddd
    return ".".join([str(addr) for addr in np.random.randint(0, 256, 4)])


def createEmailAddress():
    # USERNAME@gmail.com
    UNLength = np.random.randint(1, 11)
    username = "".join(np.random.choice(list(string.ascii_letters + string.digits), UNLength))
    return f"{username}@gmail.com"


if __name__ == "__main__":
    file = open("tests.txt", "w")
    phones, emails, ips = 0, 0, 0
    for i in range(1000):
        dType = np.random.randint(0, DATA_TYPES)
        if dType == 0:
            file.write(createPhoneNumber() + "\n")
            phones += 1
        if dType == 1:
            file.write(createEmailAddress() + "\n")
            emails += 1
        if dType == 2:
            file.write(createIPAddress() + "\n")
            ips += 1
    file.write(f"phones:{phones}, emails:{emails}, ips:{ips}")
    file.close()
