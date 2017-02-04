import requests as rq
import json
from riotApiCalls import *
from helperFunctions import *
from summonerSimpleData import *


class SummonerLiveData:

    @staticmethod
    def getLiveData(apiKey, summonerId):
        data = rq.get(RiotApiCalls.currentGame(apiKey, summonerId))

        return data.json()

    @staticmethod
    def Main():
        apiKey = HelperFunctions.getKey()
        summonerName = HelperFunctions.getSummonerNameFromUser()
        summonerIdRaw = SummonerData.getSummonerData(apiKey, summonerName)
        summonerId = summonerIdRaw[summonerName]["id"]

        data = SummonerLiveData.getLiveData(apiKey, summonerId)
        print data


if __name__ == '__main__':

    SummonerLiveData.Main()
