import unittest
from src.summonerSimpleData import *


class SummonerData_test(unittest.TestCase):

    def test_getSummonerData(self):

        result = SummonerData.getSummonerData('123abc', 'aName')
        self.assertEqual(result["status"]["status_code"], 403)
