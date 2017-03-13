import requests

# grabs some data from a station
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
