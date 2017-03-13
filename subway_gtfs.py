import requests
import json
import time
import threading
from callers import define_stops, stop_remover, url_generator

stops = define_stops()
stops = stop_remover(stops,4)
urls = url_generator(stops)





























# meow
