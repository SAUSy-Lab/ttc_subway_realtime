# a script which grabs real-time TTC subway arrival times via scraping the TTC website https://www.ttc.ca/Subway/next_train_arrivals.jsp

# Jeff Allen
# January, 2017

# import all the stuff!
import requests
import json
from pprint import pprint
import time
import threading

# open up the json with the ttc station and subway line data
with open('ttc_lines_stations.json') as data_file:
    stations = json.load(data_file)

# set this so it can be accessed in and out of functions
global out_data

# print meow!
print "meow"

# grab station-line pairs which will be used as inputs into get request URLs
stops = []
l = 0
# for each line
while l < 4:

    # number of stations on each line
    station_count = len(stations['subwayLines'][l]['subwayStations'])

    # for each station on that line
    s = 0
    while s < station_count:
        station_id = stations['subwayLines'][l]['subwayStations'][s]['id']
        line_id = stations['subwayLines'][l]['subwayStations'][s]['subwayLine']
        pair = [station_id,line_id]
        stops.append(pair)
        s += 1

    l += 1

# print meow
print "meow"

# an example of a url that we'll be scraping:  https://www.ttc.ca/Subway/loadNtas.action?subwayLine=2&stationId=42&searchCriteria=&_

# remove Scarborough RT from stops, which unfortunatly doesnt have data :(
new_stops = []
for row in stops:
    if row[1] == 4:
        None
    else:
        new_stops.append(row)
stops = new_stops

# grabbing a custom list of the urls to send
urls = []
for row in stops:
    url = "https://www.ttc.ca/Subway/loadNtas.action?subwayLine=" + str(row[1]) + "&stationId=" + str(row[0]) + "&searchCriteria=&_"
    urls.append(url)


# function for sending data request to the url
def station_request(el_url):

    # time before request was sent
    before = time.time()

    # sending / recieving the request
    r = requests.get(el_url)

    # time request was returned with data!
    after = time.time()

    # in epoch time
    grab_time = (before + after) / 2

    # convert data into json dict
    r = r.content
    r = json.loads(r)

    # grab relevant data
    data = r['ntasData']
    station = r['stationId']
    line = r['subwayLine']
    headsigns = r['defaultDirection']

    # put into a dict object
    out_row = {"grab_time": grab_time, "line":line, "station":station, "headsigns":headsigns, "times":data}

    # was it succesfull ? if so, append data to global out_data table
    out_data.append(out_row)


# putting the request in a few try brackets, since on occasion it will return null data, resending seems to work sometimes
def try_request(el_url):
    try:
        station_request(el_url)
    except:
        time.sleep(0.1)
        try:
            station_request(el_url)
        except:
            time.sleep(0.1)
            try:
                station_request(el_url)
            except:
                time.sleep(0.1)
                try:
                    station_request(el_url)
                except:
                    time.sleep(0.1)
                    try:
                        station_request(el_url)
                    except:
                        time.sleep(0.1)
                        try:
                            station_request(el_url)
                        except:
                            time.sleep(0.1)
                            try:
                                station_request(el_url)
                            except:
                                time.sleep(0.1)
                                try:
                                    station_request(el_url)
                                except:
                                    print "fail"


# loop starting time
begin = time.time()

# continue forever scraping data
t = 0
while True:

    out_data = []

    url_len = len(urls)

    l = 0

    # for each url in the list of urls
    while l < url_len:

        # start thread for scraping data
        th = threading.Thread(target=try_request,args=(urls[l],))
        th.start()

        l += 1

    # preventing proceeding if threads are still running
    x = 1
    while x < 60:
        time.sleep(1)
        if threading.active_count() == 1:
            break
        x += 1

    # sleep for 5 seconds
    time.sleep(5)

    # put everything into a dic and copy that into an output file
    dic = {"cycle":t,"data": out_data}

    with open('out_json_data/' + str(t) + '.json', 'w') as outfile:
        json.dump(dic, outfile)

    # count loops
    t += 1

    # print iteration and time since started
    print t, begin - time.time()


# cancel out when you want to quit!
