import re


# todo change all functions to work on one single email, checking lists is not necessary

def Email_Check_Bool(paragraph):  # todo change function name to fit API (isQueryEmail)
    emails = re.findall(r'([a-zA-Z0-9._-]+@[\w.-]+)', paragraph)
    if len(emails) > 0:
        for q in emails:
            if q.count("@") == 1:
                Shtrudel = q.find("@")  # todo change shtrudel varname to atSignIndex
                prefix = q[0:Shtrudel]
                count = 0
                for char in prefix:  # todo make it so when this rule is broken raise error instead of returning false
                    # todo this for loop doesn't work for example test abc..def@gmail.com
                    # todo I want this for loop to be in a seperate function prefixCheck for later use
                    if char == "." or char == "_" or char == "-":
                        count += 1
                    else:
                        count = 0
                    if count == 2:
                        break
                    return True
        return False
    return False


def Email_Check_List(paragraph):  # todo this function isn't needed since we check one email at at time
    valid_email_list = []
    emails = re.findall(r'([a-zA-Z0-9._-]+@[\w.-]+)', paragraph)
    print(emails)
    if len(emails) > 0:
        for q in emails:
            valid = True
            if q.count("@") == 1:
                Shtrudel = q.find("@")
                prefix = q[0:Shtrudel]
                count = 0
                for char in prefix:
                    if char == "." or char == "_" or char == "-":
                        count += 1
                    else:
                        count = 0
                    if count == 2:
                        valid = False
            if valid:
                valid_email_list.append(q)
    return valid_email_list


def Email_Piruk(paragraph):  # todo change function name to fit API (formatEmail)
    lister = []
    email_list = re.findall(r'([a-zA-Z0-9._-]+@[\w.-]+)', paragraph)
    for email in Email_Check_List(paragraph):
        Shtrudel = email.find("@")
        period = email.find(".")
        prefix = email[0:Shtrudel]
        domain = email[Shtrudel + 1:period]  # todo fix bug that happens for period in the prefix
        ending = email[period:]
        lister1 = [prefix, domain, ending]
        lister.append(lister1)
    for x in lister:
        print(x)  # todo no printing in functions, only in tests, return the email piruk


if __name__ == "__main__":
    # todo write more comprehensive tests, checking all the cases
    text = input("Enter paragraph:")
    print(Email_Check_Bool(text))
    print("")
    print(Email_Check_List(text))
    print("")
    Email_Piruk(text)
