import re

def Email_Check (paragraph):
    emails = re.findall(r'([a-zA-Z0-9._-]+@[\w.-]+)', paragraph)
    if (len(emails)>0):
        for q in emails:
            if (q.count("@") == 1):
                Shtrudel = q.find("@")
                prefix = q[0:Shtrudel]
                count = 0
                for char in prefix:
                    if char == "." or char == "_" or char == "-":
                        count+=1
                    else:
                        count = 0
                    if count == 2:
                        break
                    return True
        return False
    return False


def Email_Piruk(paragraph):
    lister = []
    print(paragraph)
    for email in paragraph:
        Shtrudel = email.find("@")
        period = email.find(".")
        prefix = email[0:Shtrudel]
        domain = email[Shtrudel+1:period]
        ending = email[period:]
        lister1 = [prefix, domain, ending]
        lister.append(lister1)
    for x in lister:
        print(x)


text = input("Enter paragraph:")
email_list = re.findall(r'([a-zA-Z0-9._-]+@[\w.-]+)', text)
print (Email_Check(text))
Email_Piruk(email_list)





