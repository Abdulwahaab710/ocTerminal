#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import sys


def decodeJson(jfile):
    return json.loads(jfile)


def getApiKeyAndAppId(jfile):
    '''(str) -> (str)'''
    try:
        data = ''
        with open(jfile) as data_file:
            data = json.load(data_file)
        return [data['apiKey'], data['appId']]
    except KeyError:
        print 'invalid key, or the key doesn\'t exists'
        exit()
    except IOError:
        print 'invalid file name, or the file doesn\'t exists'
        exit()


def sendRequest(busStop):
    apiKeyAndAppid = getApiKeyAndAppId('apiKey.json')
    return requests.post(
        'https://api.octranspo1.com/v1.2/GetNextTripsForStopAllRoutes',
        data={
            "appID": apiKeyAndAppid[1],
            "apiKey": apiKeyAndAppid[0],
            "stopNo": busStop,
            "format": "json"
        }
    ).json()


def busSchedule(data):
    print data['GetRouteSummaryForStopResult']['StopNo'] + " - " + str(
        data['GetRouteSummaryForStopResult']['StopDescription']
    )
    if 'Trips' in data['GetRouteSummaryForStopResult']['Routes']['Route']:
        print "\033[1;4;32mRoute " + str(
            data['GetRouteSummaryForStopResult']['Routes']['Route']['RouteNo']
        ) + "\033[0m"
        route = data['GetRouteSummaryForStopResult']['Routes']['Route']
        trips = route['Trips']['Trip']
        for trip in trips:
            print "\033[32mTrip Destination: \033[0m" + trip['TripDestination']
            print "\033[32mAdjusted Schedule Time: \033[0m " + str(
                trip['AdjustedScheduleTime']
            ) + " minutes"
    else:
        for bus in data['GetRouteSummaryForStopResult']['Routes']['Route']:
            if 'Trips' in bus and len(bus['Trips']) > 0:
                print "\033[1;4;32mRoute " + str(bus['RouteNo']) + "\033[0m"
                for trip in range(len(bus['Trips'])):
                    try:
                        print "\033[32mTrip Destination: \033[0m" + str(
                            bus['Trips'][trip]['TripDestination']
                        )
                        print "\033[32mAdjusted Schedule Time: \033[0m " + str(
                            bus['Trips'][trip]['AdjustedScheduleTime']
                        ) + " minutes"
                    except:
                        print trip


def main():
    try:
        jdata = sendRequest(sys.argv[1])
    except IndexError:
        try:
            busStop = raw_input("ENTER THE STOP NUMBER >>> ")
            while len(busStop) != 4 or not busStop.isdigit():
                busStop = raw_input("ENTER THE STOP NUMBER >>> ")
            jdata = sendRequest(busStop)
        except KeyboardInterrupt:
            print "\nBye Bye!"
            exit()
    finally:
        # print jdata
        # data = decodeJson(jdata)
        busSchedule(jdata)


if __name__ == "__main__":
    main()
