#!/bin/python

# Get Build Information for groups

import os
from saucypy import SaucyPy

def time_from_seconds(elapsed):
    mins, secs = divmod(elapsed, 60)
    hours, mins = divmod(mins, 60)
    timestring = "%d Hours %02d Minutes and %02d Seconds" % (hours, mins, secs)
    return timestring

def render_build(build):
    passed = str(build['jobs']['passed'])
    total = str(build['jobs']['finished'])
    elapsed = int(build['end_time'] - build['start_time'])
    print "Name: " + str(build['name'])
    print "Result: " + str(build['status']) + ". " + passed + " Job(s) Out Of " + total + " Passed."
    print "Total Run Time: " + time_from_seconds(elapsed)
    print '-----'

def main():
    sauceaccount = SaucyPy(os.environ['sauceuser'], os.environ['saucepass'])
    builds = sauceaccount.get_builds()
    for build in builds:
        render_build(build)

if __name__ == '__main__':
    main()
