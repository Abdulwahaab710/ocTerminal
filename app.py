#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2, json, sys

def decodeJson(jfile):
    return json.loads(jfile)

def sendRequest(busStop):
    return urllib2.urlopen("http://abdulwahaab.ca/octranspo/index.php?busNo="+str(busStop)).read()

def busSchedule(data):
    print data['GetRouteSummaryForStopResult']['StopNo'] + " - " + data['GetRouteSummaryForStopResult']['StopDescription']
    if 'Trips' in data['GetRouteSummaryForStopResult']['Routes']['Route']:
        print "\033[1;4;32mRoute " + str(data['GetRouteSummaryForStopResult']['Routes']['Route']['RouteNo']) + "\033[0m" 
        for trip in data['GetRouteSummaryForStopResult']['Routes']['Route']['Trips']['Trip']:
            print "\033[32mTrip Destination: \033[0m" + trip['TripDestination']
            print "\033[32mAdjusted Schedule Time: \033[0m " + trip['AdjustedScheduleTime'] + " minutes"
    else:
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
    try:
        jdata = sendRequest(sys.argv[1])
    except IndexError:
        try:
            busStop = raw_input("ENTER THE STOP NUMBER >>> ")
            while len(busStop) != 4 or  not busStop.isdigit():
                busStop = raw_input("ENTER THE STOP NUMBER >>> ")
        except KeyboardInterrupt:
            print "\nBye Bye!"
            exit()
    finally:
        jdata = sendRequest(busStop)
        data = decodeJson(jdata)
        busSchedule(data)


if __name__ == "__main__":
    main()
