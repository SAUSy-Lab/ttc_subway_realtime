Grabbing the real-time arrival times for trains at TTC subway stations.

#### grab_all_data.py
Python script which scrapes the TTC's next train arrival data (https://www.ttc.ca/Subway/next_train_arrivals.jsp) and returns it into json objects. It can be modified to run for a set period of time or for specific stations. It does not attempt to parse the data or do anything useful with it.

#### ttc_lines_stations.json
JSON object of all the subway stations on all 4 subway lines and operated by the TTC. This is accessed by the above Python script.
