from urllib.parse import urlparse


def link_properties(url):
    domain = urlparse(url).netloc
    domain = domain.replace("www.", "")

    protocol_name = url.split(':')[0]

    requested_page = url.split('//')[1].split('/')[-1]

    sub_folders = url.split('//')[1].split('/')[1:-1]

    return protocol_name, domain, requested_page, sub_folders
