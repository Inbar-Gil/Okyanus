"""
This file contains functions for searching phone number websites
"""
import requests as req


def phoneOwnerInformation(infoPhoneNumber):
    resp = req.get("https://441il.com/en/looktra.php?area=" + infoPhoneNumber[1][0] + "&phone=" + infoPhoneNumber[2])
    infoHtmlList = resp.text.split("<TD>")[1:]
    place = 0
    for i in infoHtmlList:
        indexSymbol = infoHtmlList[place].index("<")
        infoHtmlList[place] = infoHtmlList[place][:indexSymbol]
        place += 1

    #Returns: Name, Adress
    return [infoHtmlList[3], infoHtmlList[4]]


print(phoneOwnerInformation(["ed", ("08",), "6272343"]))
