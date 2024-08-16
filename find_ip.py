import re


def findip_in_string(string):
    a = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',string).group()
    return a
