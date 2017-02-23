import json
from parseInGameData import *


class RageLevels:

	@staticmethod
	def rageLevels(enemyList, championRageData):

		rageLevelList = []
		for enemy in enemyList:
			rageLevelList.append(int((championRageData["championIds"][str(enemy)]["rageLevel"])) / 10.0)

		chanceOfRage = ((sum(rageLevelList) / len(rageLevelList)) * 100)
		return chanceOfRage


	@staticmethod
	def Main():
		championRageData = json.load(open('./sample_rage_level.json'))
		inGameData = InGameData.Main()
		chanceOfRage = RageLevels.rageLevels(inGameData[1], championRageData)

		print "There is a %" + str(chanceOfRage) + " chance of rage."

if __name__ == "__main__":

	RageLevels.Main()