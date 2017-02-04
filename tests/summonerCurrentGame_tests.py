import unittest
from src.summonerCurrentGame import *


class SummonerLiveData_test(unittest.TestCase):

    def test_getLiveData(self):

        result = SummonerLiveData.getLiveData('123abc', '456')
        self.assertEqual(result["status"]["status_code"], 403)
