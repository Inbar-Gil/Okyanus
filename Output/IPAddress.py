"""
This file contains functions for searching IP websites
"""
import urllib.request


def searchIPInfo(IP):
    request_url = urllib.request.urlopen('http://ipinfo.io/'+IP+'?token=c2b88a2d6f552a')
    print(request_url.read())




def searchIPAPI(IP):

    request_url = urllib.request.urlopen('http://ip-api.com/json/'+ IP)
    print(request_url.read())


def getIPResponse(IP):
    """
    #"isp","org","as"
    #hostname - loc
    :param IP:
    :return: all data
    """


searchIPInfo("221.119.149.238")
searchIPAPI("221.119.149.238")