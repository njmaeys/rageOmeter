import requests as rq
import json
from riotApiCalls import *
from helperFunctions import *


class SummonerData:

    @staticmethod
    def getSummonerData(apiKey, summonerName):
        data = rq.get(RiotApiCalls.summonerIdUrl(apiKey, summonerName))

        return data.json()

    @staticmethod
    def Main():
        apiKey = HelperFunctions.getKey()
        summonerName = HelperFunctions.getSummonerNameFromUser()

        data = SummonerData.getSummonerData(apiKey, summonerName)
        
        return data


if __name__ == "__main__":

    SummonerData.Main()
