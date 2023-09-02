import csv

def readData(path: str) -> dict:
    with open(path, 'r',encoding="utf-8") as file:
        spreader = csv.reader(file)
        for row in spreader:
            print(row)

            
if __name__ == "__main__":
    readData("assets/data/val_stats.csv")