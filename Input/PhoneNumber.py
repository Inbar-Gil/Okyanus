"""
Contains the functions for analyzing phone numbers
"""

import re

PHONE_NUMBER_TYPE = {1: "Intl", 2: "Mobl", 3: "Home"}


def isQueryPhoneNumber(query):
    # Remove white characters
    pattern = re.compile(r'\s+')
    query = re.sub(pattern, '', query)

    phoneIntl = re.match(r'\+\d{3}-?[0-9]{7}([0-9]{2})?([0-9])?', query, re.IGNORECASE)
    phoneMobileOrHome = re.match(r'\d{3}-?\d{3}-?\d{4}', query, re.IGNORECASE)
    oldPhoneHomeNumber = re.match(r'0[23489]-?\d{3}-?\d{4}', query, re.IGNORECASE)

    return isMatchPhoneNumber(query, phoneMobileOrHome) or isMatchPhoneNumber(query,
                                                                              phoneIntl) or isMatchPhoneNumber(
        query, oldPhoneHomeNumber)


def isMatchPhoneNumber(query, finalSearchPhoneNumber):
    return finalSearchPhoneNumber != None and finalSearchPhoneNumber.group(0) == query


def formatPhoneNumber(query):
    """
    :returns [PHONE_TYPE, (PREFIXES), DIGITS]
    """


def findPhoneNumberType(phoneNumber):
    # *** Get phone number assuming it is OK ***

    digitsHomePhoneNumber = [2, 3, 4, 7, 8, 9]

    if phoneNumber[0] == "+":
        return PHONE_NUMBER_TYPE[1]
    if int(phoneNumber[1]) in digitsHomePhoneNumber:
        return PHONE_NUMBER_TYPE[3]
    return PHONE_NUMBER_TYPE[2]
