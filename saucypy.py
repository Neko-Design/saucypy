#!/bin/python

# SaucyPy Interface to SauceLabs API
# Written by Ewen McCahon, 2016
# Version 0.0.1

import json
import requests
from requests.auth import HTTPBasicAuth

SAUCE_BASE_URL = 'https://saucelabs.com/rest/v1'

def auth(user, token):
    authblock = {'userid': user, 'token': token}
    return authblock

def makeWebRequest(auth, url, payload=''):
    if payload:
        try:
            response = requests.post(url, auth=(auth['userid'], auth['token']), json=payload)
        except:
            print "Something went wrong posting to" + url
    else:
        try:
            response = requests.get(url, auth=(auth['userid'], auth['token']))
        except:
            print "Something went wrong making a request to" + url
    try:
        responseJson = response.json()
    except ValueError:
        print "Invalid JSON returned"
    return responseJson

def makeApiRequest(auth, api):
    compiledURL = SAUCE_BASE_URL + api
    apiResponse = makeWebRequest(auth, compiledURL)
    return apiResponse

def makePostRequest(auth, api, payload=''):
    compiledURL = SAUCE_BASE_URL + api
    apiResponse = makeWebRequest(auth, compiledURL, payload)
    return apiResponse

def getSubAccounts(auth):
    apiCall = '/users/' + auth['userid'] + '/subaccounts'
    apiResponse = makeApiRequest(auth, apiCall)
    return apiResponse

def getSiblingAccounts(auth):
    apiCall = '/users/' + auth['userid'] + '/siblings'
    apiResponse = makeApiRequest(auth, apiCall)
    return apiResponse

def createUser(auth, userName, password, email, fullName):
    apiCall = '/users/' + auth['userid']
    jp = {'username': userName, 'password': password, 'name': fullName, 'email': email}
    apiResponse = makePostRequest(auth, apiCall, jp)
    return apiResponse

def getBuilds(auth):
    apiCall = '/' + auth['userid'] + '/builds'
    apiResponse = makeApiRequest(auth, apiCall)
    return apiResponse

def getBuild(auth, buildId):
    apiCall = '/' + auth['userid'] + '/builds/' + buildId
    apiResponse = makeApiRequest(auth, apiCall)
    return apiResponse

if __name__ == "__main__":
    print "SaucyPy Interface to SauceLabs API"
