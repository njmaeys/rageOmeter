import os


class HelperFunctions:

    @staticmethod
    def getKey():
        with open('../riotApiKey.txt', 'r') as k:
            key_file = k.read()

        return key_file.strip()

    @staticmethod
    def getSummonerNameFromUser():
        summonerName = raw_input("Enter summoner name: ")

        return summonerName.lower().replace(' ', '')
