"""
This file contains functions for searching IP websites
"""
import json
import urllib.request

from ..API.API import Site
from typing import Dict
from typing import Union

TOKEN = "c2b88a2d6f552a"


class Ipinfo(Site):

    def searchSite(self) -> Dict[str, str]:
        keys = ["hostname", "city", "region", "loc"]
        data_file = self.searchIPInfo()
        Info_dict = json.loads(data_file)
        try:
            output_dic = {key: Info_dict[key] for key in keys}
            return output_dic
        except Exception:
            return dict()

    def searchIPInfo(self) -> Union[str, bytes]:
        request_url = urllib.request.urlopen(f"http://ipinfo.io/{self.data}?token={TOKEN}")
        return request_url.read()


class IpApi(Site):
    def searchIPAPI(self) -> Union[str, bytes]:
        request_url = urllib.request.urlopen(f"http://ip-api.com/json/{self.data}")
        return request_url.read()

    def searchSite(self) -> Dict[str, str]:
        keys = ["isp", "org", "as"]
        data_file = self.searchIPAPI()
        Api_Dict = json.loads(data_file)
        try:
            output_dic = {key: Api_Dict[key] for key in keys}
            return output_dic
        except Exception:
            return dict()


def searchIp(Ip: str) -> Dict[str, str]:
    ip_info = Ipinfo(Ip)
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
