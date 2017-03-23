import requests
import json
import time
import threading
import priors
import requesters

# get the initial setups
stops = priors.define_stops()
stops = priors.stop_remover(stops,4)
urls = priors.url_generator(stops)

try:
    requesters.station_request(urls[2])
except:
    None



























# meow
