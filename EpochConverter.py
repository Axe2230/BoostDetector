import calendar
import time
import datetime

# Convert from human-readable date to epoch in following format '2000-01-01' (YEAR-MONTH-DAY)
def convertToEpoch(humanTime=None):
    epochTime = calendar.timegm(time.strptime(humanTime, '%Y-%m-%d'))
    return epochTime

# Convert from Epoch to human-readable date '2000-01-01' (YEAR-MONTH-DAY)
def convertFromEpoch(epochTime=None):
    humanTime = datetime.datetime.utcfromtimestamp(epochTime)
    return humanTime.__str__()[:10]


# epoch = (convertToEpoch('2023-02-13'))
# print("Epoch Time: ", epoch)
#
# print("Human Time: ", convertFromEpoch(epoch))
