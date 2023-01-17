#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status
use the package urllib
 body of the response must be displayed in tabulation before -
"""
import requests
r = requests.get('https://alx-intranet.hbtn.io/status')
resp = r.text
print('Body response:\n\t- type: {}'.format(type(resp)))
print('\t- content: {}'.format(resp))
