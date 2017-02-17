import json


# TODO pass this from the live game data api call
summonerName = 'doubleliftfanboy'

# TODO get this data from the api call not the static temp file
rawData = open('./sample_in_game_data.json', 'r').read()
data = json.loads(rawData)

currentGameSummoners = data["participants"]

def getTargetSummonerData(summonerData):
	targetData = []

	for summoner in summonerData:
		if summoner["summonerName"] == summonerName:
			targetTeam = summoner["teamId"]
			targetChampionId = summoner["championId"]

			targetData.append(targetTeam)
			targetData.append(targetChampionId)

	return targetData

targetSummonerData = getTargetSummonerData(currentGameSummoners)
print targetSummonerData

def getEnemyTeamData(summonerData, targetSummonerTeamId):
	allEnemyData = []

	for enemy in summonerData:
		if enemy["teamId"] != targetSummonerTeamId:
			allEnemyData.append(enemy)

	return allEnemyData

enemyData = getEnemyTeamData(currentGameSummoners, targetSummonerData[0])
print enemyData