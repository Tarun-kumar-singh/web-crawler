from urllib.parse import urlparse


def get_domian_name(url):
    try:
        sub_domain_array = get_sub_domain_name(url).split('.')
        return sub_domain_array[-2] + '.' + sub_domain_array[-1]
    except():
        return ''


def get_sub_domain_name(url):

    try:
        return urlparse(url).netloc
    except():
        return ''


