"""
contains the code which analyzes the query and chooses the sites to search
"""
from .EMail import EMail
from .IPAddress import IP
from .PhoneNumber import Phone
from .Username import Username
from typing import Tuple

class RegExAnalyzer:
    def __init__(self, query:str):
        self.query = query
        self.queryType = ""
        self.data = []

    def getQueryType(self) -> None:
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

    def returnData(self) -> tuple[str,list]:
        return self.queryType, self.data
