"""
This file contains functions for searching IP websites
"""
import urllib.request
import json
from API.API import Site


class Ipinfo(Site):
    def __init__(self, query):
        super().__init__(query)

    def searchSite(self):
        output_dic = {}
        data_file = self.searchIPInfo()
        Info_dict = json.loads(data_file)
        for i in Info_dict.keys():
            if i == "hostname":
                output_dic[i] = Info_dict[i]
            if i == "city":
                output_dic[i] = Info_dict[i]
            if i == "region":
                output_dic[i] = Info_dict[i]
            if i == "loc":
                output_dic[i] = Info_dict[i]
        return output_dic

    def searchIPInfo(self):
        request_url = urllib.request.urlopen('http://ipinfo.io/' + self.data + '?token=c2b88a2d6f552a')
        return request_url.read()


class IpApi(Site):
    def __init__(self, query):
        super().__init__(query)

    def searchIPAPI(self):
        request_url = urllib.request.urlopen('http://ip-api.com/json/' + self.data)
        return request_url.read()

    def searchSite(self):
        output_dic = {}
        data_file = self.searchIPAPI()
        Api_Dict = json.loads(data_file)
        for i in Api_Dict.keys():
            if i == "isp":
                output_dic[i] = Api_Dict[i]
            if i == "org":
                output_dic[i] = Api_Dict[i]
            if i == "as":
                output_dic[i] = Api_Dict[i]
        return output_dic


def searchIp(Ip):
    ip_info = Ipinfo(Ip)
    info_dict = ip_info.searchSite()
    ip_api = IpApi(Ip)
    api_dict = ip_api.searchSite()
    info_dict.update(api_dict)

    return info_dict


x = searchIp("8.8.8.8")

