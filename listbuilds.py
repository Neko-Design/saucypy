#!/bin/python

# Get Build Information for groups

import os
import saucypy

SAUCE_ACCOUNT = saucypy.auth(os.environ['sauceuser'], os.environ['saucepass'])

def render_build(build):
    passed = str(build['jobs']['passed'])
    total = str(build['jobs']['finished'])
    print "Name: " + str(build['name'])
    print "Result: " + str(build['status']) + ". " + passed + " Job(s) Out Of " + total + " Passed."
    print

def main():
    builds = saucypy.getBuilds(SAUCE_ACCOUNT)
    for build in builds:
        render_build(build)

if __name__ == '__main__':
    main()
