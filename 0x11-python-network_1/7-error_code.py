#!/usr/bin/python3
"""
takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and finally displays the body of the response
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.post(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))