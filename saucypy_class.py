#!/bin/python

# SaucyPy Interface to SauceLabs API
# Written by Ewen McCahon, 2016
# Version 0.0.1

import json
import requests
from requests.auth import HTTPBasicAuth

class saucypy:

    # Main Vars
    SAUCE_BASE_URL = 'https://saucelabs.com/rest/v1'

    # Init Func
    def __init__(self, sauceuser, saucepass):
        self.auth = {'userid': sauceuser, 'token': saucepass}

    def make_web_request(self, url, payload=''):
        if payload:
            try:
                response = requests.post(url, auth=(self.auth['userid'],
                                                    self.auth['token']), json=payload)
            except:
                print "Something went wrong posting to" + url
        else:
            try:
                response = requests.get(url, auth=(self.auth['userid'], self.auth['token']))
            except:
                print "Something went wrong making a request to" + url
        try:
            response_json = response.json()
        except ValueError:
            print "Invalid JSON returned"
        return response_json

    def make_api_request(self, api):
        compiled_url = self.SAUCE_BASE_URL + api
        api_response = self.make_web_request(compiled_url)
        return api_response

    def make_post_request(self, api, payload=''):
        compiled_url = self.SAUCE_BASE_URL + api
        api_response = self.make_web_request(compiled_url, payload)
        return api_response
