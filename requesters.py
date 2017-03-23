import requests
import time
import json

# grabs some data from a station
def station_request(el_url):

    # time before request was sent
    before = time.time()

    # sending / recieving the request
    r = requests.get(el_url[2])

    # time request was returned with data!
    after = time.time()

    # in epoch time
    grab_time = (before + after) / 2

    # convert data into json dict
    r = r.content
    r = json.loads(r)

    # grab relevant data
    t1 = r['ntasData'][0]['trainId']
    t2 = r['ntasData'][3]['trainId']
    i1 = r['ntasData'][0]['timeInt']
    i2 = r['ntasData'][3]['timeInt']
    # t1 = r['ntasData'][3]['trainId']
    # t2 = r['ntasData'][3]['trainId']
    # t1 = r['ntasData'][3]['trainId']
    # t2 = r['ntasData'][3]['trainId']
    station = r['stationId']
    line = r['subwayLine']


    print el_url[0], el_url[1]
    print t1, i1
    print t2, i2
    print station, line, grab_time

    #return out_row
