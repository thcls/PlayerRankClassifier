import csv
from json import dump, load

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
    
def test():
    dataList = getJsonData("assets/data/json/val_stats.json")
    
    minList = []
    maxList = []
    
    keyList = ['damage_round','headshots','headshot_percent','aces','clutches','flawless','first_bloods','kills','deaths','assists','kd_ratio','kills_round','most_kills','score_round','wins','win_percent','gun1_head','gun1_body','gun1_legs','gun2_head','gun2_body','gun2_legs','gun3_head','gun3_body','gun3_legs']
    
    itemList = dict(zip(keyList, [float(1000000000000000000000000000000)]*len(keyList)))
    
    for i in range(len(dataList)):
        for key in keyList:
            if dataList[i][key] < itemList[key]:
                print('itfjd')
                itemList[key] = dataList[i][key]
                
    print(itemList)
    
def minList():
    return {'damage_round': 0.0, 'headshots': 0.0, 'headshot_percent': 0.0, 'aces': 0.0, 'clutches': 0.0, 'flawless': 0.0, 'first_bloods': 0.0, 'kills': 0.0, 'deaths': 3.0, 'assists': 0.0, 'kd_ratio': 0.0, 'kills_round': 0.0, 'most_kills': 0.0, 'score_round': 0.0, 'wins': 0.0, 'win_percent': 0.0, 'gun1_head': 0.0, 'gun1_body': 0.0, 'gun1_legs': 0.0, 'gun2_head': 0.0, 'gun2_body': 0.0, 'gun2_legs': 0.0, 'gun3_head': 0.0, 'gun3_body': 0.0, 'gun3_legs': 0.0}
    
def maxList():
    return {'damage_round': 340.6, 'headshots': 5261.0, 'headshot_percent': 83.3, 'aces': 24.0, 'clutches': 488.0, 'flawless': 316.0, 'first_bloods': 1296.0, 'kills': 6016.0, 'deaths': 5048.0, 'assists': 1932.0, 'kd_ratio': 6.5, 'kills_round': 2.0, 'most_kills': 58.0, 'score_round': 550.5, 'wins': 170.0, 'win_percent': 100.0, 'gun1_head': 100.0, 'gun1_body': 100.0, 'gun1_legs': 50.0, 'gun2_head': 100.0, 'gun2_body': 100.0, 'gun2_legs': 100.0, 'gun3_head': 100.0, 'gun3_body': 100.0, 'gun3_legs': 100.0}

if __name__ == "__main__":
    dataList = getJsonData("assets/data/json/val_stats.json")

    print(countData(dataList))
