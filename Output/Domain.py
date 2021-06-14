import json
import whois11
from typing import Dict
from ..API.API import Site

START_AT = 300


def is_not_empty(string):
    return string != "" and string != " "


def is_person(string, index):
    if string[index:index + 7] == "person:":
        return True
    else:
        return False


def edit_result_to_dict(result):
    dictionary = {}
    lines = list(filter(is_not_empty, result.split("\n")))
    for line in lines:
        filtered_line = list(filter(is_not_empty, line.split(" ")))

        if filtered_line[0] in dictionary:
            dictionary[filtered_line[0]] += ", " + " ".join(filtered_line[1:])
        else:
            dictionary[filtered_line[0]] = " ".join(filtered_line[1:])

    return dictionary


def get_whois(domain):
    full_result = whois11.whois(domain)

    first_ind = full_result.find("person", START_AT)

    if first_ind == -1 or not is_person(full_result, first_ind):
        return dict()

    second_ind = full_result.find("person", first_ind + 1)

    if second_ind == -1:
        second_ind = full_result.find("registrar name", first_ind + 1)

    result = full_result[first_ind:second_ind]

    return edit_result_to_dict(result)


class WhoisAPI(Site):
    def searchSite(self) -> dict:
        self.response = get_whois(self.data[0])
        return self.response


def searchDomain(data: tuple) -> Dict[str, str]:
    if data[1]:
        return {"domain": data[1].upper()}
    else:
        wi_site = WhoisAPI(data=data)
        response = wi_site.searchSite()
        if response == {}:
            raise ValueError("No Domain Data")
        else:
            return response
