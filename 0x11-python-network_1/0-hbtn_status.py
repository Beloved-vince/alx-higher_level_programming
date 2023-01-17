#!/usr/bin/python3
"""
This  Python script that fetches https://alx-intranet.hbtn.io/status
Using  the package urllib
"""

import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as html:
        result = html.read()
        print("Body response:")
        print("\t - type: {}".format(type(result)))
        print('\t - content: {}'.format(result))
        print("\t - utf8 content: {}".format(result.decode("utf8")))
