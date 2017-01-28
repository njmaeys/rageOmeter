import requests as rq
import riot_api_calls as rac
import helper_functions as hf
import json


key = hf.get_key_file()

data = rq.get(rac.champion_live_data(key))
rawData = data.json()
print rawData
