#!/usr/bin/python3
"""
This  Python script that fetches https://alx-intranet.hbtn.io/status
Using  the package urllib
"""
import urllib.request


with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    result = response.read()