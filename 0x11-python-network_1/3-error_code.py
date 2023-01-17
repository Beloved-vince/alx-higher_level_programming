#!/usr/bin/python3
"""
given URL & email as params, send POST req to URL, display response body utf-8
usage: ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
"""
from sys import argv
import urllib.parse
import urllib.request


if __name__ == '__main__':
    url = argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as resp:
            print(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))