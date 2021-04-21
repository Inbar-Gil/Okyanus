"""
Contains the functions for analyzing phone numbers
"""

import re


def isQueryPhoneNumber(query):
    #Remove white characters
    pattern = re.compile(r'\s+')
    query = re.sub(pattern, '', query)

    phoneIntl = re.match(r'\+\d{3}-?\d{9}', query, re.IGNORECASE)
    phoneMobileOrHome = re.match(r'\d{3}-?\d{3}-?\d{4}', query, re.IGNORECASE)

    return isMatchPhoneNumber(query, phoneMobileOrHome) or isMatchPhoneNumber(query, phoneIntl)


def isMatchPhoneNumber(query, finalSerachPhoneNumber):
    return finalSerachPhoneNumber != None and finalSerachPhoneNumber.group(0) == query

