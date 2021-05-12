"""
contains the code which analyzes the query and chooses the sites to search
"""
from Input.EMail import EMail
from Input.IPAddress import IP
from Input.PhoneNumber import Phone
from Input.Username import Username


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
        Ip = IP(self.query).getQueryData()
        PhoneNum = Phone(self.query).getQueryData()
        User = Username(self.query).getQueryData()
        if email[0]:
            self.queryType = "EMAIL"
            self.data = email[1]

        elif Ip[0]:
            self.queryType = "IP"
            self.data = Ip[1]

        elif PhoneNum[0]:
            self.queryType = "PHONE"
            self.data = PhoneNum[1]

        elif User[0]:
            self.queryType = "USERNAME"
            self.data = User[1]
        else:
            raise ValueError("This username is illegal")

    def returnData(self):
        return self.queryType, self.data


if __name__ == "__main__":
    with open("../Tests/RegExTests.txt") as f:
        list = f.readlines()
        for test in list:
            test = test.split("\n")
            temp = RegExAnalyzer(test[0])
            try:
                 temp.getQueryType()
                 print (temp.returnData())
            except ValueError:
                print ("Invalid query: " + temp.query)