"""
contains the code which analyzes the query and chooses the sites to search
"""
from Input.EMail import EMail
from Input.IPAddress import IP
from Input.PhoneNumber import Phone

class RegExAnalyzer:
    def __init__(self, query):
        self.query = query
        self.queryType = ""
        self.data = []

    def getQueryType(self):
        """
        checks all types to see which type the query is
        sets query type and data accordingly
        :return:
        """
        email = EMail(self.query).getQueryData()
        if email[0]:
            self.queryType = "EMAIL"
            self.data = email[1]
        Ip = IP(self.query).getQueryData()
        if Ip[0]:
            self.queryType = "IP"
            self.data = Ip[1]
        PhoneNum = Phone(self.query).getQueryData()
        if PhoneNum[0]:
            self.queryType = "PHONE"
            self.data = PhoneNum[1]

    def returnData(self):
        return self.queryType, self.data


if __name__ == "__main__":
    query = RegExAnalyzer(input("ENTER QUERY: "))
    query.getQueryType()
    print (query.returnData())

