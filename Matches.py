import requests
import Requests
from Summoner import *
from EpochConverter import *

# Ranked Flex = 440 queue ID
# Ranked Solo = 420 queue ID
# Normal Draft Pick = 400 queue ID
# Normal Blind Pick = 430 queue ID
# We'll be using Draft/Blind pick performance and Previous Ranked Performance
def urlBuilder(puuid, start="0", count="20", startTime=None, endTime=None, queue=None, type="ranked"):
    url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/" + puuid + "/ids?startTime="+startTime+"&endTime="+endTime+"&queue="+queue+"&type="+type+"&start="+start+"&count="+count
    return url
class Matches:
  def __init__(self, puuid, start, count, startTime=None, endTime=None, queue=None, type="ranked"):
    try:
        url = urlBuilder(puuid, str(start), str(count), str(startTime), str(endTime), str(queue), type)
        response = requests.get(url, headers=Requests.headers)
        status_code = response.status_code
        response = response.json()
        print(response)
        if status_code == 200:
            self.status = 200
            self.matchesList = response
            self.puuid = puuid
        else:
            self.status = status_code
            print(response)
    except:
        print("Something went wrong, please try again")

def main():
    # --------------------Grabbing User Inputs---------------------------------
    # summonerNameInput = str(input("Enter Summoner Name: "))
    # summoner = Summoner(summonerNameInput)
    # startDate = str(input("Enter start date in following format '2000-01-01' (YEAR-MONTH-DAY): "))
    # endDate = str(input("Enter end date in following format '2000-01-01' (YEAR-MONTH-DAY): "))
    # queue = str(input("Enter queue id (Flex=440, RankedSolo=420, NormalDraft=400, NormalBlind=430): "))
    # type = str(input("Enter type (normal, ranked): "))
    #
    # matchList = Matches(summoner.puuid, 0, 20, convertToEpoch(startDate), convertToEpoch(endDate), queue, type)

    # TESTING
    matchList = Matches("q3sXj01K8JDXD958Ul4AcSngfZAaDv6PIxV3EFwzn6Oy46OEeXPR6ZT416U4Gl2Pogn8Xkops8rpPQ", 0, 20,
                        1676073600, 1676246400, 400, "normal")

if __name__ == "__main__":
    main()