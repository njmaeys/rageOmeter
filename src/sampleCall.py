import requests as rq
import riot_api_calls as rac
import helper_functions as hf
import json


key = hf.get_key_file()

data = rq.get('https://na.api.pvp.net/api/lol/na/v1.2/champion?api_key='+key)
rawData = data.json()
print rawData
