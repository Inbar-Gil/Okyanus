from domain_temp.Link import  *


def urlProperties(domain):
    social_list = [domain]
    if domain == "www.facebook.com":
        social_list.append("Facebook link")
    if domain == "www.instagram.com":
        social_list.append("Instagram link")
    if domain == "twitter.com":
        social_list.append("Twitter link")
    return social_list


def url_properties(domain):
    if domain == "facebook.com":
        return "Facebook"
    if domain == "instagram.com":
        return "Instagram"
    if domain == "twitter.com":
        return "Twitter"
    return None


if __name__ == "__main__":
    print(repr(urlparse("https://www.facebook.com/groups/1461656040797270/user/100005066730592/").netloc))
    domain = link_properties("https://www.facebook.com/groups/1461656040797270/user/100005066730592/")
    print(domain)
    print(repr(url_properties(domain)))
