#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value of the
variable Email in the response header
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.post(argv[1], data={"key": argv[2]})
    print("Your email is".format(r.headers.get(argv[2])))
