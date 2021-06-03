"""
This file contains functions for searching IP websites
"""
import urllib.request
import json
from ..API.API import Site

TOKEN = "c2b88a2d6f552a"


class IpInfo(Site):

    def searchIPInfo(self):
        request_url = urllib.request.urlopen('http://ipinfo.io/' + self.data + '?token=' + TOKEN)
        return request_url.read()

    def searchSite(self):
        keys = ["hostname", "city", "region", "loc"]
        data_file = self.searchIPInfo()
        Info_dict = json.loads(data_file)
        try:
            output_dic = {key: Info_dict[key] for key in keys}
            return output_dic
        except Exception:
            return dict()


class IpApi(Site):

    def searchIPAPI(self):
        request_url = urllib.request.urlopen('http://ip-api.com/json/' + self.data)
        return request_url.read()

    def searchSite(self):
        keys = ["isp", "org", "as"]
        data_file = self.searchIPAPI()
        Api_Dict = json.loads(data_file)
        try:
            output_dic = {key: Api_Dict[key] for key in keys}
            return output_dic
        except Exception:
            return dict()


def searchIp(Ip):
    ip_info = IpInfo(Ip)
    info_dict = ip_info.searchSite()
    ip_api = IpApi(Ip)
    api_dict = ip_api.searchSite()
    info_dict.update(api_dict)
    if info_dict != {}:
        return info_dict
    else:
        raise ValueError


if __name__ == '__main__':

    x = searchIp("0.0.0.0")
    print(x)
