class RiotApiCalls:

    @staticmethod
    def get_key(api_key_file):
        with open(api_key_file, 'r') as k:
            key = k.read()
            return key

    @staticmethod
    def summonerIdUrl(key, summoner_name):
        summoner_url = ('https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/'+summoner_name+'?api_key='+key)
        return summoner_url

    @staticmethod
    def mostMostPlayedChamp(key, summonerId):
        most_played_champions = ('https://na.api.pvp.net/championmastery/location/NA1/player/'+str(summonerId)+'/topchampions?count=5&api_key='+key)
        return most_played_champions

    @staticmethod
    def championFromStaticData(key, champId):
        champ_name_url = ('https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/'+str(champId)+'?champData=image&api_key='+key)
        return champ_name_url

    @staticmethod
    def summonerTier(key, champId):
        champ_ranking_url = ('https://na.api.pvp.net/api/lol/na/v2.5/league/by-summoner/'+str(champId)+'/entry?api_key='+key)
        return champ_ranking_url

    @staticmethod
    def summonerKDA(key, champId):
        ranked_data_url = ('https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/'+str(champId)+'/ranked?season=SEASON2016&api_key='+key)
        return ranked_data_url

    @staticmethod
    def summonerRankedWinsLosses(key, champId):
        ranked_win_loss_url = ('https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/'+str(champId)+'/summary?season=SEASON2016&api_key='+key)
        return ranked_win_loss_url

    @staticmethod
    def recentMatchData(key, champId):
        recent_match_data = ('https://na.api.pvp.net/api/lol/na/v1.3/game/by-summoner/'+str(champId)+'/recent?api_key='+key)
        return recent_match_data

    @staticmethod
    def championLiveData(key):
        champion_url = ('https://na.api.pvp.net/api/lol/na/v1.2/champion?api_key='+key)
        return champion_url

    @staticmethod
    def currentGame(key, summonerId):
        url = ('https://na.api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/NA1/'+str(summonerId)+'?api_key='+key)
        return url
