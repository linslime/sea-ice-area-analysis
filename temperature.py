import pandas as pd
import csv

data = []
list = []
result = []

def readdata():
    global data
    global list
    global result
    df = pd.read_excel(r'D:\Desktop\温度数据.xls', sheet_name='Sheet1')
    data = df.values.tolist()
    list = [[[] for j in range(12)] for i in range(45)]
    key  = type(data[0][0])
    for i in range(len(data)):
        for j in range(0,len(data[i])):
            if type(data[i][j]) == key :
                list[data[i][j].year - 1978][data[i][j].month - 1].append(data[i][j+1])
    result = [[i + 1978,j + 1,sum(list[i][j])/len(list[i][j])] for i in range(45) for j in range(12) if len(list[i][j]) != 0]

def writecsv(x):
    with open("D:\Desktop\\temperature.csv", "w" , newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(x)

if __name__ == "__main__":
    readdata()
    # writecsv(result)
    print(data)
