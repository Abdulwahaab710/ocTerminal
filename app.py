#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2, json, sys

def decodeJson(jfile):
    return json.loads(jfile)

def sendRequest(busStop):
    if busStop == "":
        busStop = raw_input("ENTER THE STOP NUMBER")

    return urllib2.urlopen("http://abdulwahaab.ca/octranspo/index.php?busNo="+str(busStop)).read()

def busSchedule(data):
    for bus in data['GetRouteSummaryForStopResult']['Routes']['Route']:
        if 'Trips' in bus and len(bus['Trips']) > 0:
            print "\033[1;4;32mRoute " + str(bus['RouteNo']) + "\033[0m"
            for trip in range(len(bus['Trips'])):
                try:
                    print "\033[32mTrip Destination: \033[0m" + bus['Trips'][trip]['TripDestination']
                    print "\033[32mAdjusted Schedule Time: \033[0m " + bus['Trips'][trip]['AdjustedScheduleTime'] + " minutes"
                except:
                    print trip


def main():
    jdata = sendRequest(sys.argv[1])
    data = decodeJson(jdata)
    busSchedule(data)


if __name__ == "__main__":
    main()