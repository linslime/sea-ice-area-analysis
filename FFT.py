import pandas as pd
import math
from matplotlib import pyplot as plt
from scipy.fftpack import fft,ifft
import numpy as np
import csv

data = []

def readdata():
    global data
    df = pd.read_excel(r'D:\Desktop\N_Sea_Ice_Index_Regional_Monthly_Data_G02135_v3.0.xls', sheet_name='St-Lawrence-Area-km^2')
    data = df.values.tolist()[2:]
    data = [i[1::2] for i in data]
    data = [i  for j in data for i in j if math.isnan(i) == False]

def writescv(x):
    with open("D:\Desktop\St-Lawrence-Area-km^2.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(x)

if __name__ == "__main__":
    readdata()
    data_fft = fft(data)
    data_fft = np.abs(data_fft)
    writescv(data_fft)
    plt.plot(data_fft)
    plt.show()
    # print( (data[108] ) )
