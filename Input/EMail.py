import re
from API.API import QueryType

class EMail(QueryType):

    def isQueryType(self):
        if re.match(r'[a-zA-Z0-9._-]+@[\w.-]+',self.query):
            count = 0
            atSignIndex = self.query.find("@")
            prefix = self.query[0:atSignIndex]
            for char in prefix:
                if char == "." or char == "_" or char == "-":
                    count += 1
                else:
                    count = 0
                if count == 2:
                    raise ValueError("This email is not legal")
            self.state = True
        return False


    def formatQuery(self):
        atSignIndex = self.query.find("@")
        afterAtSignIndex = self.query[atSignIndex:]
        periodSignIndex = afterAtSignIndex.find(".")
        prefix = self.query[0:atSignIndex]
        domain = afterAtSignIndex[1:periodSignIndex]
        ending = afterAtSignIndex[periodSignIndex:]
        self.data = [prefix, domain, ending]

if __name__ == "__main__":
    query = input("Enter paragraph:")
    email = EMail(query)
    print (email.getQueryData())
