"""
This file contains functions for searching phone number websites
"""
import requests as req
from ..API.API import Site
from typing import List, Union, Dict

NO_RESPONSE = 'NONE'


class PhoneNumber441(Site):
    def searchSite(self) -> Union[List[str, str], str]:
        """
        searches the relevant Site and gets the response
        :return: the site's response
        self.data - list of the info -> phone number
        """
        try:
            resp = req.get(
                "https://441il.com/en/looktra.php?area=" + self.data[1][0] + "&phone=" + self.data[
                    2])
            infoHtmlList = resp.text.split("<TD>")[1:]
            place = 0
            for _ in infoHtmlList:
                indexSymbol = infoHtmlList[place].index("<")
                infoHtmlList[place] = infoHtmlList[place][:indexSymbol]
                place += 1

            # Returns: Name, Address

            return [infoHtmlList[3], infoHtmlList[4]]
        except Exception:
            print("No Response\n")


def searchPhoneNumber(data: str) -> Dict[str, str]:
    """
    This function create dictionary that contains the name and the address of the owner
    :return: dict
    """
    p1 = PhoneNumber441(data)
    listInfo = p1.searchSite()
    dictInfo = {"Name": listInfo[0], "Address": listInfo[1]}
    return dictInfo
