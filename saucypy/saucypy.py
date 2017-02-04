#!/bin/python

# SaucyPy Interface to SauceLabs API
# Written by Ewen McCahon, 2016
# Version 0.0.5

import json
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    print "SaucyPy Interface to SauceLabs API"

class SaucyPy:
    """
    SaucyPy
    Main Controller for SaucyPy wrapper
    Makes it much easier to use the SauceLabs API
    usage: saucypy('username', 'api token')
    """

    # Main Vars
    SAUCE_BASE_URL = 'https://saucelabs.com/rest/v1'

    # Init Func
    def __init__(self, sauceuser, saucepass):
        self.auth = {'userid': sauceuser, 'token': saucepass}

    def make_web_request(self, url, payload=''):
        """
        Make Web Request
        Takes parameters and submits HTTP requests
        """
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
        """
        Make API Request
        Get Wrapper for main HTTP lib
        """
        compiled_url = self.SAUCE_BASE_URL + api
        api_response = self.make_web_request(compiled_url)
        return api_response

    def make_post_request(self, api, payload=''):
        """
        Make Post request
        Post Wrapper for main HTTP lib
        """
        compiled_url = self.SAUCE_BASE_URL + api
        api_response = self.make_web_request(compiled_url, payload)
        return api_response

    # Account Information Functions
    def get_child_accounts(self):
        """
        Get SubAccounts
        Lists child accounts of caller
        usage: get_child_accounts()
        """
        api_call = '/users/' + self.auth['userid'] + '/subaccounts'
        api_response = self.make_api_request(api_call)
        return api_response

    def get_sibling_accounts(self):
        """
        Get Sibling Accounts
        Lists all accounts sharing the same parent as the caller
        usage: get_sibling_accounts()
        """
        api_call = '/users/' + self.auth['userid'] + '/siblings'
        api_response = self.make_api_request(api_call)
        return api_response

    def create_user(self, user_name, password, email, full_name):
        """
        Create User
        Generates a new user in SauceLabs under the calling account
        usage: create_user('username', 'password', 'email', 'full name')
        """
        api_call = '/users/' + self.auth['userid']
        json_packet = {'username': user_name, 'password': password,
                       'name': full_name, 'email': email}
        api_response = self.make_post_request(api_call, json_packet)
        return api_response

    # Build Information Functions
    def get_builds(self):
        """
        Get Builds
        Lists all builds run from the caller
        usage: get_builds()
        """
        api_call = '/' + self.auth['userid'] + '/builds'
        api_response = self.make_api_request(api_call)
        return api_response

    def get_build(self, build_id):
        """
        Get Build
        Returns a single build based on ID or name
        usage: get_build('build id or name)
        """
        api_call = '/' + self.auth['userid'] + '/builds/' + build_id
        api_response = self.make_api_request(api_call)
        return api_response

    def search_builds(self, build_string):
        """
        Search Build
        Returns all builds matching a name search
        usage: search_builds('build name fragment')
        """
        all_builds = self.get_builds()
        matching_builds = []
        for build in all_builds:
            if build_string in build['name']:
                matching_builds.append(build)
        return matching_builds

    # SauceLabs Status Functions
    def get_sauce_status(self):
        """
        Get SauceLabs Status
        Returns SauceLabs Status information
        usage: get_sauce_status()
        """
        api_call = '/info/status'
        api_response = self.make_api_request(api_call)
        return api_response

    def get_sauce_platforms(self):
        """
        Get SauceLabs Platforms
        Returns SauceLabs Available Platforms
        usage: get_sauce_platforms()
        """
        api_call = '/info/platforms/all'
        api_response = self.make_api_request(api_call)
        return api_response
