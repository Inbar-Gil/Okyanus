"""
Contains the functions for analyzing phone numbers
"""

import re

PHONE_NUMBER_TYPE = {1: "Intl", 2: "Mobl", 3: "Home"}
OLD_PHONE_LEN = 9
END_PREFIX_INTL = 4
END_PREFIX_HOME_MOBL = 3


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
    prefixes = []
    digits = ""
    phoneType = findPhoneNumberType(query)
    query = query.replace("-", "").replace("\n", "")
    if phoneType == "Intl":
        prefixes.append(query[:END_PREFIX_INTL])
        prefixes.append('0' + query[END_PREFIX_INTL:6])
        digits = query[7:]
    elif phoneType == "Mobl":
        prefixes.append(query[:END_PREFIX_HOME_MOBL])
        digits = query[END_PREFIX_HOME_MOBL:]
    else:
        if len(query) == OLD_PHONE_LEN:
            prefixes.append(query[:END_PREFIX_HOME_MOBL - 1])
            digits = query[END_PREFIX_HOME_MOBL:]
        else:
            prefixes.append(query[:END_PREFIX_HOME_MOBL])
            digits = query[END_PREFIX_HOME_MOBL:]

    return [phoneType, tuple(prefixes), digits]


def findPhoneNumberType(phoneNumber):
    # *** Get phone number assuming it is OK ***

    digitsHomePhoneNumber = [2, 3, 4, 7, 8, 9]

    if phoneNumber[0] == "+":
        return PHONE_NUMBER_TYPE[1]
    if int(phoneNumber[1]) in digitsHomePhoneNumber:
        return PHONE_NUMBER_TYPE[3]
    return PHONE_NUMBER_TYPE[2]
