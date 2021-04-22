import re


# todo change all functions to work on one single email, checking lists is not necessary

def fit_API(isQueryEmail):  # todo change function name to fit API (isQueryEmail)
    email = re.findall(r'([a-zA-Z0-9._-]+@[\w.-]+)', isQueryEmail)
    email = "".join(email)
    return email


def prefix_Check(preFormatEmail):
    if preFormatEmail.count("@") == 1:
        count = 0
        atSignIndex = preFormatEmail.find("@")  # todo change shtrudel varname to atSignIndex
        prefix = preFormatEmail[0:atSignIndex]
        for char in prefix:  # todo make it so when this rule is broken raise error instead of returning false
            # todo this for loop doesn't work for example test abc..def@gmail.com
            # todo I want this for loop to be in a seperate function prefixCheck for later use
            if char == "." or char == "_" or char == "-":
                count += 1
            else:
                count = 0
            if count == 2:
                raise ValueError("This email is not legal")
        return True
    raise ValueError("This email is not legal")


def format_Email(formatEmail):
    atSignIndex = formatEmail.find("@")
    afterAtSignIndex = formatEmail[atSignIndex:]
    periodSignIndex = afterAtSignIndex.find(".")
    prefix = formatEmail[0:atSignIndex]
    domain = afterAtSignIndex[1:periodSignIndex]
    ending = afterAtSignIndex[periodSignIndex:]
    lister1 = [prefix, domain, ending]
    return lister1


if __name__ == "__main__":
    # todo write more comprehensive tests, checking all the cases
    text = input("Enter paragraph:")
    if (prefix_Check(fit_API(text))):
        formattedEmail = fit_API(text)
        print(format_Email(formattedEmail))
