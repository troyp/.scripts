#!/usr/bin/env python

from __future__ import print_function
import requests
import json

GITHUB_BASE_API = "https://api.github.com"


def main(user):
    response = requests.get("{}/users/{}/repos".format(GITHUB_BASE_API, user))
    for repo in response.json():
        print(repo['name'])


if __name__ == '__main__':
    import plac
    plac.call(main)
