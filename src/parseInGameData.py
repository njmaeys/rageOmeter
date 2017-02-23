import json
from summonerCurrentGame import *

runLocal = True

class InGameData:

	@staticmethod
	def getTargetSummonerData(summonerData, summonerName):
		currentGameSummoners = summonerData["participants"]
		targetData = []

		for summoner in currentGameSummoners:
			if summoner["summonerName"].lower().replace(' ', '') == summonerName:
				targetTeam = summoner["teamId"]
				targetChampionId = summoner["championId"]

				targetData.append(targetTeam)
				targetData.append(targetChampionId)

		return targetData

	@staticmethod
	def getEnemyTeamData(summonerData, targetSummonerTeamId):
		allEnemyData = []
		data = summonerData["participants"]

		for enemy in data:
			if enemy["teamId"] != targetSummonerTeamId:
				allEnemyData.append(enemy)

		return allEnemyData

	@staticmethod
	def getEnemyTeamChampions(enemyData):
		enemyChampions = []

		for enemy in enemyData:
			championId = enemy["championId"]
			enemyChampions.append(championId)

		return enemyChampions


	@staticmethod
	def Main():
		if runLocal:
			rawData = json.load(open('../leagueCurrentGame.json'))	
			summonerName = 'heisendong'
			targetSummonerData = InGameData.getTargetSummonerData(rawData, summonerName)
			enemyData = InGameData.getEnemyTeamData(rawData, targetSummonerData[0])
			championIds = InGameData.getEnemyTeamChampions(enemyData)

			return (targetSummonerData, championIds)
		else:
			getLiveData = SummonerLiveData.Main()
			summonerName = getLiveData[0]
			rawData = getLiveData[1]

			if "status" in rawData:
				print "Summoner not in game."	
			else:
				targetSummonerData = InGameData.getTargetSummonerData(rawData, summonerName)
				enemyData = InGameData.getEnemyTeamData(rawData, targetSummonerData[0])
				championIds = InGameData.getEnemyTeamChampions(enemyData)

				return (targetSummonerData, championIds)

if __name__ == "__main__":

	InGameData.Main()