import unittest
import StringIO
from src.summonerCurrentGame import *


class SummonerLiveData_test(unittest.TestCase):

    def test_getLiveData(self):

        result = SummonerLiveData.getLiveData('123abc', '456')
        self.assertIsNotNone(result)
