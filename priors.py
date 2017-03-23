# grabbing arrays of stops, line numbers, and, urls to call

import json

# grabs list of stops from the json input
def define_stops():

    # grab json with stops
    with open('ttc_lines_stations.json') as data_file:
        stations = json.load(data_file)

    stops = []

    l = 0

    while l < 4:

        # number of stations on each line
        station_count = len(stations['subwayLines'][l]['subwayStations'])

        # for each station on that line
        s = 0
        while s < station_count:
            station_id = stations['subwayLines'][l]['subwayStations'][s]['id']
            line_id = stations['subwayLines'][l]['subwayStations'][s]['subwayLine']
            name = stations['subwayLines'][l]['subwayStations'][s]['name']
            pair = [station_id,line_id,name]
            stops.append(pair)
            s += 1

        l += 1

    return stops

# removes lines with no data
def stop_remover(stop_array,line_number):
    new_stops = []
    for row in stop_array:
        if row[1] == line_number:
            None
        else:
            new_stops.append(row)
    return new_stops


# generates urls to call data from with stops and lines
def url_generator(stop_array):
    urls = []
    for row in stop_array:
        url = "https://www.ttc.ca/Subway/loadNtas.action?subwayLine=" + str(row[1]) + "&stationId=" + str(row[0]) + "&searchCriteria=&_"
        urls.append([row[0],row[1],url])
    return urls
