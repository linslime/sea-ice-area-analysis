import pandas as pd
import math
import csv

data = []
list = []
result = []

def readdata():
    global data
    global list
    global result
    df = pd.read_excel(r'D:\Desktop\slr_sla_gbl_keep_txj1j2_90 (1).xls', sheet_name='slr_sla_gbl_keep_txj1j2_90 (1)')
    data = df.values.tolist()[5:]
    list = [[[] for j in range(12)] for i in range(int(data[-1][0]) - int(data[0][0]) + 1)]
    for i in range(len(data)):
        year = int(data[i][0])
        month = int((data[i][0] - int(data[i][0])) * 12)
        for j in range(1,5):
            if math.isnan(data[i][j]) == False:
                list[year - int(data[0][0])][month].append(data[i][j])
                break

    result = [[i + int(data[0][0]),j + 1,sum(list[i][j])/len(list[i][j])] for i in range(int(data[-1][0]) - int(data[0][0]) + 1) for j in range(12) if len(list[i][j]) != 0]

def writecsv(x):
    with open("D:\Desktop\Sealevel1.csv", "w" , newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(x)

if __name__ == "__main__":
    readdata()
    print(data)
    print(list)
    print(len(list))
    print(len(list[0]))
    print(result)
    writecsv(result)