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
        if (
            data['apiKey'] == 'Your API key' or data['appId'] == 'Your APP ID'
        ):
            raise NameError('Invalid key, or the key doesn\'t exists')
        else:
            return [data['apiKey'], data['appId']]
    except KeyError:
        print 'Invalid key, or the key doesn\'t exists'
        exit()
    except IOError:
        print 'Invalid file name, or the file doesn\'t exists'
        exit()
    except NameError:
        print 'Invalid key, or the key doesn\'t exists'
        sys.exit()


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
    jdata = ""
    try:
        jdata = sendRequest(sys.argv[1])
        busSchedule(jdata)
    except IndexError:
        try:
            busStop = raw_input("ENTER THE STOP NUMBER >>> ")
            while len(busStop) != 4 or not busStop.isdigit():
                busStop = raw_input("ENTER THE STOP NUMBER >>> ")
            jdata = sendRequest(busStop)
            busSchedule(jdata)
        except KeyboardInterrupt:
            print "\nBye Bye!"
            exit()


if __name__ == "__main__":
    main()
