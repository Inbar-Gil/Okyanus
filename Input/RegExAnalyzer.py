"""
contains the code which analyzes the query and chooses the sites to search
"""
from Input.EMail import EMail
from Input.IPAddress import IP
from Input.EMail import Phone

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

    def returnData(self):
        return self.queryType, self.data


if __name__ == "__main__":
    with open("tests.txt", 'r') as f:
        lines = f.readlines()
