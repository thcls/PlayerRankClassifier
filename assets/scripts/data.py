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

def dataNumberToFloat() -> None:
    dataList = getJsonData("assets/data/json/val_stats.json")
    for i in range(len(dataList)):
        for key in dataList[i].keys():
            try:
                dataList[i][key] = float(dataList[i][key])
            except:
                pass
                
    setJsonData("assets/data/json/val_stats.json", dataList)
    
if __name__ == "__main__":
    pass