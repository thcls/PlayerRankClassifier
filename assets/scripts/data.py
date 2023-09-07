import csv
from json import dump, load
from random import randint

def readData(path: str) -> dict:
    dataList = []
    
    with open(path, 'r',encoding="utf-8-sig") as file:
        spreader = csv.DictReader(file, quoting=csv.QUOTE_NONNUMERIC)
        for line in spreader:
            dataList.append(line)
            
    return dataList
            
def countData(dataList: list) -> dict:
    rankList = []
    rankNumber = []
    
    for line in dataList:
        lineTest = True
        for i in range(len(rankList)):
            if line['rating'] == rankList[i]:
                rankNumber[i] += 1
                lineTest = False
                break
        if lineTest:
            rankList.append(line['rating'])
            rankNumber.append(1)
            
    countList = dict(zip(rankList, rankNumber))
    return countList

def setJsonData(dataPath: str, dataList: list) -> None:
    with open(dataPath, "w", encoding="utf-8-sig") as file:     
        dump(dataList, file)

def getJsonData(dataPath: str) -> list:
    with open(dataPath, "r", encoding="utf-8-sig") as file:     
        dataList = load(file)
    return dataList

def dataNumberToFloat(dataPath: str, dataList: list) -> None:
    dataList = getJsonData(dataPath)
    for i in range(len(dataList)):
        for key in dataList[i].keys():
            try:
                dataList[i][key] = float(dataList[i][key])
            except:
                pass
                
    setJsonData(dataPath, dataList)
    
def minList() -> list:
    return {'damage_round': 0.0, 'headshots': 0.0, 'headshot_percent': 0.0, 'aces': 0.0, 'clutches': 0.0, 'flawless': 0.0, 'first_bloods': 0.0, 'kills': 0.0, 'deaths': 3.0, 'assists': 0.0, 'kd_ratio': 0.0, 'kills_round': 0.0, 'most_kills': 0.0, 'score_round': 0.0, 'wins': 0.0, 'win_percent': 0.0, 'gun1_head': 0.0, 'gun1_body': 0.0, 'gun1_legs': 0.0, 'gun1_kills': 0.0, 'gun2_head': 0.0, 'gun2_body': 0.0, 'gun2_legs': 0.0, 'gun2_kills': 0.0, 'gun3_head': 0.0, 'gun3_body': 0.0, 'gun3_legs': 0.0, 'gun3_kills': 0.0}
    
def maxList() -> list:
    return {'damage_round': 340.6, 'headshots': 5261.0, 'headshot_percent': 83.3, 'aces': 24.0, 'clutches': 488.0, 'flawless': 316.0, 'first_bloods': 1296.0, 'kills': 6016.0, 'deaths': 5048.0, 'assists': 1932.0, 'kd_ratio': 6.5, 'kills_round': 2.0, 'most_kills': 58.0, 'score_round': 550.5, 'wins': 170.0, 'win_percent': 100.0, 'gun1_head': 100.0, 'gun1_body': 100.0, 'gun1_legs': 50.0, 'gun1_kills': 3845.0, 'gun2_head': 100.0, 'gun2_body': 100.0, 'gun2_legs': 100.0, 'gun2_kills': 1279.0, 'gun3_head': 100.0, 'gun3_body': 100.0, 'gun3_legs': 100.0, 'gun3_kills': 650.0}

def allKeys() -> list:
    return [ 'damage_round', 'headshots', 'headshot_percent', 'aces', 'clutches', 'flawless', 'first_bloods', 'kills', 'deaths', 'assists', 'kd_ratio', 'kills_round', 'most_kills', 'score_round', 'wins', 'win_percent', 'gun1_head', 'gun1_body', 'gun1_legs', 'gun1_kills', 'gun2_head', 'gun2_body', 'gun2_legs', 'gun2_kills', 'gun3_head', 'gun3_body', 'gun3_legs', 'gun3_kills']
    #['region', 'name', 'tag', 'rating', 'damage_round', 'headshots', 'headshot_percent', 'aces', 'clutches', 'flawless', 'first_bloods', 'kills', 'deaths', 'assists', 'kd_ratio', 'kills_round', 'most_kills', 'score_round', 'wins', 'win_percent', 'agent_1', 'agent_2', 'agent_3', 'gun1_name', 'gun1_head', 'gun1_body', 'gun1_legs', 'gun1_kills', 'gun2_name', 'gun2_head', 'gun2_body', 'gun2_legs', 'gun2_kills', 'gun3_name', 'gun3_head', 'gun3_body', 'gun3_legs', 'gun3_kills']for key in keyList:

def normalize(dataList: dict) -> None:
    maxL = maxList()
    minL = minList()
    
    keyList = allKeys()
    
    for i in range(len(dataList)):
        for key in keyList:
            x = dataList[i][key]
            x = (x - minL[key]) / (maxL[key] - minL[key])
            
            dataList[i][key] = x
            
def prob(total: int, y: int) -> str:
    return "{:.2f}%".format((100*y)/total)

def test(testList: dict, testAnswers: dict) -> str:
    total = len(testList)
    right = 0
    ranks = countData(testList)
    rankProb = {'Radiant': 0,
                'Immortal 3': 0, 
                'Immortal 2': 0, 
                'Immortal 1': 0}
    
    for i in range(total):
        if testList[i]["rating"] == testAnswers[i]["rating"]:
            right += 1
            rankProb[testAnswers[i]["rating"]] += 1
            print(f"Precisão de {prob(total, right)}")
            
    for key in rankProb.keys():
        rankProb[key] = prob(ranks[key], rankProb[key])
        
    msg = f"{rankProb} = {prob(total, right)}"
    
    print(msg)
    
    return msg
    
def getTestList(dataList: dict) -> list:
    testList = []
    
    ranks = {'Radiant': 529,
            'Immortal 3': 2222, 
            'Immortal 2': 4209, 
            'Immortal 1': 10427}

    while ranks['Radiant'] != 0 or ranks['Immortal 1'] != 0 or ranks['Immortal 2'] != 0 or ranks['Immortal 3'] != 0:
        index = randint(0, len(dataList)-1)
        rank = dataList[index]["rating"]
        
        if ranks.get(rank,-1) != -1 and ranks[rank] != 0:
            print(f"{ranks} ____ {rank}")
            player = dataList.pop(index)
            ranks[rank] -= 1
            testList.append(player)
    
    print(countData(dataList))
    print(len(testList))
    print(countData(testList))
    return testList

if __name__ == "__main__":
    dataList = getJsonData("assets/data/json/val_stats.json")
    
    print(countData(dataList))