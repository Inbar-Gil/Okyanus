import requests
import json
import whois11

START_AT = 300


def request_thingy(domain):
    x = requests.post("https://www.whois11.com/fetch/fast-whois", data={"domain": "amazon.com"},
                      headers={
                          "content-length": "17",
                          "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                          "path": "/fetch/fast-whois",
                          "origin": "https://www.whois11.com",
                          "referer": "https://www.whois11.com/domain-whois"})

    print(x.text)

    dict = json.loads(x.text)

    for key in dict:
        print(key, ":", dict[key])
        print("___")

    website_ip = dict["ip"]

    response = requests.post(f"https://ipapi.co/{website_ip}/json/", data={}, headers={"authority": "ipapi.co",
                                                                                       "path": f"/{website_ip}/json/",
                                                                                       "accept-language": "en-US,en;q=0.9",
                                                                                       "origin": "https://www.whois11.com",
                                                                                       "referer": "https://www.whois11.com/"})

    print("_______\n_________\nSTARTING SECOND")
    print(response.text)


def is_not_empty(string):
    return string != "" and string != " "


def is_person(string, index):
    # print("CHECK: ", string[index:index+7])
    if string[index:index + 7] == "person:":
        # print("TRUE")
        return True
    else:
        # print("FALSE")
        return False


def edit_result_to_dict(result):
    dictionary = {}
    lines = list(filter(is_not_empty, result.split("\n")))
    for line in lines:
        filtered_line = list(filter(is_not_empty, line.split(" ")))
        # print(filtered_line)

        if filtered_line[0] in dictionary:
            dictionary[filtered_line[0]] += ", " + " ".join(filtered_line[1:])
        else:
            dictionary[filtered_line[0]] = " ".join(filtered_line[1:])

    # print("dict: ", dictionary)
    return dictionary


def get_whois(domain):
    full_result = whois11.whois(domain)
    print(full_result)

    first_ind = full_result.find("person", START_AT)
    # print("first in: ", first_ind)

    if first_ind == -1 or not is_person(full_result, first_ind):
        return dict()

    second_ind = full_result.find("person", first_ind + 1)

    if second_ind == -1:
        second_ind = full_result.find("registrar name", first_ind + 1)

    result = full_result[first_ind:second_ind]

    return edit_result_to_dict(result)


if __name__ == '__main__':
    print(get_whois("n12.co.il"))
