import requests
import Requests

class Summoner:
  def __init__(self, name):
    try:
        url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name
        response = requests.get(url, headers=Requests.headers)
        status_code = response.status_code
        # print(response)
        response = response.json()
        if status_code == 200:
            self.status = 200
            self.id = response['id']
            self.accountId = response['accountId']
            self.puuid = response['puuid']
            self.name = name
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


viperclutch = Summoner("Viper Clutch")
viperclutch.printInfo()