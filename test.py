#!/bin/python

# Tests for SaucyPy
# Really basic at the moment.
# TODO Rewrite in proper framework

import sys
import os
import saucypy

sauceaccount = saucypy.auth(os.environ['sauceuser'], os.environ['saucepass'])

tp = 0
tf = 0

def sep():
    print("========================================================")

def show_title(title):
    sep()
    print("[TEST] " + title)
    sep()

def passed():
    global tp
    print("[TEST] PASSED")
    tp = tp + 1

def failed():
    global tf
    print("[TEST] FAILED")
    tf = tf + 1

def info(string):
    print("[INFO] " + string)

def results():
    global tp
    global tf
    sep()
    info("Tests Passed: " + str(tp))
    info("Tests Failed: " + str(tf))
    sep()

def test_fails(fls):
    global tf
    tf = fls

# List Sibling Accounts
show_title("List Sibling Accounts")
accounts = saucypy.getSiblingAccounts(sauceaccount)
if len(accounts) > 0:
    passed()
for account in accounts:
    info(account['first_name'] + " " + account['last_name'] + ", " + account['email'])

# List Child Accounts
show_title("List Child Accounts")
childAccounts = saucypy.getSubAccounts(sauceaccount)
if len(childAccounts) > 0:
    passed()
for account in childAccounts:
    info(account['name'] + ", " + account['email'])

# Create Child Account
show_title("Create Child Account")
childAccount = saucypy.createUser(sauceaccount, "SaucyPy-Testing-User", "testing_password", "test_email@compuserve.com", "Sauce Testing 2")
if 'errors' in childAccount:
    info(str(childAccount))
    failed()
else:
    info(childAccount['id'] + " Created")
    passed()

results()
if tf > 0:
    sys.exit(1)
