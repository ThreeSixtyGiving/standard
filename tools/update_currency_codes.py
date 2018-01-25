"""
Updates the currency codelist from ISO4217 files.
Adapted from https://github.com/open-contracting/standard/ \
blob/1.1/standard/schema/utils/fetch_currency_codelist.py
"""

import json
import re
from collections import OrderedDict

import requests
from lxml import etree


def get_and_parse_xml(url):
    return etree.fromstring(requests.get(url).content)


# "List one: Current currency & funds code list"
# https://www.currency-iso.org/en/home/tables/table-a1.html
current_codes = []
tree = get_and_parse_xml('https://www.currency-iso.org/dam/downloads/lists/list_one.xml')
for node in tree.xpath('//CcyNtry'):
    match = node.xpath('./Ccy')
    # Entries like Antarctica have no universal currency.
    if match:
        code = node.xpath('./Ccy')[0].text
        title = node.xpath('./CcyNm')[0].text.strip()
        if code not in current_codes:
            current_codes.append(code)

# "List three: List of codes for historic denominations of currencies & funds"
# https://www.currency-iso.org/en/home/tables/table-a3.html
historic_codes = {}
tree = get_and_parse_xml('https://www.currency-iso.org/dam/downloads/lists/list_three.xml')
for node in tree.xpath('//HstrcCcyNtry'):
    code = node.xpath('./Ccy')[0].text
    title = node.xpath('./CcyNm')[0].text.strip()
    valid_until = node.xpath('./WthdrwlDt')[0].text
    # Use ISO8601 interval notation.
    valid_until = re.sub(r'^(\d{4})-(\d{4})$', r'\1/\2', valid_until.replace(' to ', '/'))
    if code not in current_codes:
        if code not in historic_codes:
            historic_codes[code] = {'Valid Until': valid_until}
        # If the code is historical, use the most recent
        elif valid_until > historic_codes[code]['Valid Until']:
            historic_codes[code] = {'Valid Until': valid_until}

historic_codes = list(historic_codes.keys())

with open('../schema/360-giving-schema.json') as fp:
    schema = json.load(fp, object_pairs_hook=OrderedDict)

codes = sorted(current_codes + historic_codes)
schema['definitions']['currency']['enum'] = codes

with open('../schema/360-giving-schema.json', 'w') as fp:
    json.dump(schema, fp, indent=2)
