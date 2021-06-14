"""
This file contains functions for searching phone number websites
"""
import requests as req

from ..API.API import Site
from typing import List, Dict

NO_RESPONSE = 'NONE'


class PhoneNumber441(Site):
    def searchSite(self) -> Dict[str, str]:
        """
        searches the relevant Site and gets the response
        :return: the site's response
        self.data - list of the info -> phone number
        """
        try:
            resp = req.get(f"https://441il.com/en/looktra.php?area={self.data[1][0]}&phone={self.data[2]}")
            infoHtmlList = resp.text.split("<TD>")[1:]
            place = 0
            for _ in infoHtmlList:
                indexSymbol = infoHtmlList[place].index("<")
                infoHtmlList[place] = infoHtmlList[place][:indexSymbol]
                place += 1

            # Returns: Name, Address
            return {"Name": infoHtmlList[3], "Address": infoHtmlList[4]}
        except Exception:
            raise ValueError


def searchPhoneNumber(data: tuple) -> Dict[str, str]:
    """
    This function create dictionary that contains the name and the address of the owner
    :return: dict
    """
    p1 = PhoneNumber441(data)
    dictInfo = p1.searchSite()
    return dictInfo


if __name__ == '__main__':
    print(PhoneNumber441(("ed", ("04",), "6272343")).searchSite())
    print(searchPhoneNumber(("ed", ("04",), "6272343")))
