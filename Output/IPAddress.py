"""
This file contains functions for searching IP websites
"""
import urllib.request
import json


def searchIPInfo(IP):
    request_url = urllib.request.urlopen('http://ipinfo.io/'+IP+'?token=c2b88a2d6f552a')
    return request_url.read()




def searchIPAPI(IP):

    request_url = urllib.request.urlopen('http://ip-api.com/json/'+ IP)
    return request_url.read()


def getIPResponse(IP):
    output_dic = {}
    data_file = searchIPAPI(IP)
    data_file2 = searchIPInfo(IP)
    Ip_dict = json.loads(data_file)
    Ip_dict2 = json.loads(data_file2)
    for i in Ip_dict2.keys():
        if i == "hostname":
            output_dic[i] = Ip_dict2[i]
        if i == "city":
            output_dic[i] = Ip_dict2[i]
        if i == "region":
            output_dic[i] = Ip_dict2[i]
        if i == "loc":
            output_dic[i] = Ip_dict2[i]

    for i in Ip_dict.keys():
        if i == "isp":
            output_dic[i] = Ip_dict[i]
        if i == "org":
            output_dic[i] = Ip_dict[i]
        if i == "as":
            output_dic[i] = Ip_dict[i]

    print(output_dic)



getIPResponse("221.119.149.238")
