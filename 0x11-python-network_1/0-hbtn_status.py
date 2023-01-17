#!/usr/bin/python3
"""A script that
fetches https://intranet.hbtn.io/status.
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as resp:
        content = resp.read()
        print("Body response:")
        print("    - type: {}".format(type(content)))
        print("    - content: {}".format(content))
        print("    - utf8 content: {}".format(content.decode('utf-8')))
