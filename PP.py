import pandas as pd
import math
from arch.unitroot import PhillipsPerron
from matplotlib import pyplot as plt

data = []

def readdata():
    global data
    df = pd.read_excel(r'D:\Desktop\N_Sea_Ice_Index_Regional_Monthly_Data_G02135_v3.0.xls', sheet_name='St-Lawrence-Area-km^2')
    data = df.values.tolist()[2:]
    data = [i[1::2] for i in data]
    data = [i  for j in data for i in j if math.isnan(i) == False]


if __name__ == "__main__":
    readdata()
    pp = PhillipsPerron(data)
    print(pp.summary().as_text())
    plt.plot(data)
    plt.show()
    # print( (data[108] ) )
