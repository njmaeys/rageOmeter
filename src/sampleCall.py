import requests as rq
import riot_api_calls as rac
import helper_functions as hf
import json


key = hf.get_key_file()

# TODO add in an call to a summoner id rather than hard coding in one to pass to the api
data = rq.get(rac.currentGame(key, '20411671'))
rawData = data.json()
print rawData
