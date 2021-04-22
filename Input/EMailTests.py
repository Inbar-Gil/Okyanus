import re


def isQueryEmail(query):  # todo this should be a boolean function
    email = re.findall(r'([a-zA-Z0-9._-]+@[\w.-]+)', query)
    email = "".join(email)
    return email


def prefix_Check(preFormatEmail):
    if preFormatEmail.count("@") == 1:
        count = 0
        atSignIndex = preFormatEmail.find("@")
        prefix = preFormatEmail[0:atSignIndex]
        for char in prefix:
            if char == "." or char == "_" or char == "-":
                count += 1
            else:
                count = 0
            if count == 2:
                raise ValueError("This email is not legal")
        return True
    raise ValueError("This email is not legal")


def formatEmail(query):
    atSignIndex = query.find("@")
    afterAtSignIndex = query[atSignIndex:]
    periodSignIndex = afterAtSignIndex.find(".")
    prefix = query[0:atSignIndex]
    domain = afterAtSignIndex[1:periodSignIndex]
    ending = afterAtSignIndex[periodSignIndex:]
    lister1 = [prefix, domain, ending]
    return lister1


if __name__ == "__main__":
    query = input("Enter paragraph:")
    if prefix_Check(isQueryEmail(query)):
        formattedEmail = isQueryEmail(query)
        print(formatEmail(formattedEmail))
