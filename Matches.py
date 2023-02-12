import requests
import Requests

class Matches:
  def __init__(self, puuid, start=0, count=20, ):
    try:
        url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/" + puuid + "/ids?queue=2&start=0&count=20&api_key=RGAPI-dff58ed2-2295-4fbb-a631-41de3e703f93"
        response = requests.get(url, headers=Requests.headers)
        status_code = response.status_code
        # print(response)
        response = response.json()
        if status_code == 200:
            self.status = 200
            # self.id = response['id']
            # self.accountId = response['accountId']
            # self.puuid = response['puuid']
            # self.name = name
        else:
            self.status = status_code
            print(response)
    except:
        print("Something went wrong, please try again")

  def printInfo(self):
    if self.status == 200:
        print("------------------------------")
        print("Summoner Name: " + self.name)
        print("id: " + self.id)
        print("accountID: " + self.accountId)
        print("puuid: " + self.puuid)
        print("------------------------------")