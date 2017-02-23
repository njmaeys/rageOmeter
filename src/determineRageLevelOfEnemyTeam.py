import json
from parseInGameData import *

inGameData = InGameData.Main()

rageLevels = json.load(open('./sample_rage_level.json'))

enemyChampionIds = inGameData[1]

rageLevelList = []
for enemy in enemyChampionIds:
	rageLevelList.append(int((rageLevels["championIds"][str(enemy)]["rageLevel"])) / 10.0)


chanceOfRage = ((sum(rageLevelList) / len(rageLevelList)) * 100)

print "There is a %" + str(chanceOfRage) + " chance of rage."