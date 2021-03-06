# -*- coding: utf-8 -*-
"""Crossover Strategy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1buWAV_KY17-dnNSa6BLwLa6F0ie7hwN8
"""

import pandas as pd
import numpy as np
import datetime as datetime
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Getting data
from google.colab import files
uploadedData = files.upload()

#Store data
aapl = pd.read_csv('CSV.csv')
aapl

#Visualized data
plt.figure(figsize=(16.5,4.5))
plt.plot(aapl['Adj Close'], label = 'AAPL')
plt.title('Apple Adj. Close Price History')
plt.xlabel('January 02, 2018 - July 31, 2020')
plt.ylabel('Adj. Close Price USD ($)')
plt.legend(loc='upper left')
plt.show()

#Simple Moving avg, 30 day window
SMA30 = pd.DataFrame()
SMA30['Adj Close'] = aapl['Adj Close'].rolling(window=30).mean()
SMA30

#Simple Moving avg, 100 day avg
SMA100 = pd.DataFrame()
SMA100['Adj Close'] = aapl['Adj Close'].rolling(window=100).mean()
SMA100

#Visualzed 
plt.figure(figsize=(16.5,4.5))
plt.plot(aapl['Adj Close'], label = 'AAPL')
plt.plot(SMA30['Adj Close'], label = 'SMA30')
plt.plot(SMA100['Adj Close'], label = 'SMA100')
plt.title('Apple Adj. Close Price History')
plt.xlabel('January 02, 2018 - July 31, 2020')
plt.ylabel('Adj. Close Price USD ($)')
plt.legend(loc='upper left')
plt.show()

#Data frame to store all data
data = pd.DataFrame()
data['AAPL'] = aapl['Adj Close']
data['SMA30'] = SMA30['Adj Close']
data['SMA100'] = SMA100['Adj Close']
data

#Function for when to buy or sell
def buy_sell(data):
  sigPriceBuy = []
  sigPriceSell = []
  count = -1

  for i in range(len(data)):
    if data['SMA30'][i] > data['SMA100'][i]: #Buy Signal
      if count !=1:
        sigPriceBuy.append(data['AAPL'][i])
        sigPriceSell.append(np.nan)
        count = 1
      else:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)
    elif data['SMA30'][i] < data['SMA100'][i]: #Sell Signal
      if count != 0:
          sigPriceBuy.append(np.nan)
          sigPriceSell.append(data['AAPL'][i])
          count = 0
      else:
          sigPriceBuy.append(np.nan)
          sigPriceSell.append(np.nan)
    else:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)

  return(sigPriceBuy, sigPriceSell)

#Store buy and sell
buy_sell = buy_sell(data)
data['Buy_Signal_Price'] = buy_sell[0]
data['Sell_Signal_Price'] = buy_sell[1]

#Show data
data

#Visualize data and strategy
plt.figure(figsize=(16.5,4.5))
plt.plot(data['AAPL'], label = 'AAPL', alpha = 0.35)
plt.plot(data['SMA30'], label = 'SMA30', alpha = 0.35)
plt.plot(data['SMA100'], label = 'SMA100', alpha = 0.35)
plt.scatter(data.index, data['Buy_Signal_Price'], label = 'Buy', marker = '^', color = 'green')
plt.scatter(data.index, data['Sell_Signal_Price'], label = 'Sell', marker = 'v', color = 'red')
plt.title('Apple Adj. Close Price History Buy & Sell Signals')
plt.xlabel('January 02, 2018 - July 31, 2020')
plt.ylabel('Adj. Close Price USD ($)')
plt.legend(loc='upper left')
plt.show