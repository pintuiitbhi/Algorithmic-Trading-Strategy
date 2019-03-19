import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import math
import datetime
import time
import os

quandl.ApiConfig.api_key = 'Ufux_HxUXZKAgFjxWhGi'
my_year_month_fmt = mdates.DateFormatter('%m/%y')

def fetch_historical_data(ticker,end_date):

    data = quandl.get("WIKI/"+ticker, start_date ='2016-01-01' ,end_date  = end_date) #backtest

    cwd = os.getcwd()
    data.to_csv(os.path.join(cwd,'database/historicaldat.csv'),index=True,header=True)
    return data

def plot_historical_data(ticker,start_date,end_date):
    # import matplotlib.pyplot as plt
    # %matplotlib notebook
    quandl.ApiConfig.api_key = 'Ufux_HxUXZKAgFjxWhGi'
    data = quandl.get(["WIKI/"+ticker+".1","WIKI/"+ticker+".4"], start_date =start_date ,end_date  = end_date)
    fig= plt.figure(figsize=(8,6))
    ax1=fig.add_subplot(111,ylabel="Price")
    # ax1.subplot()
    data["WIKI/"+ticker+' - Close'].plot(ax=ax1,color='b',lw=.8)
    signals=pd.DataFrame(index=data.index)
    print("Close plot window to continue")
    data.head()
    signals['sma']=data["WIKI/"+ticker+' - Close'].rolling(5).mean()
    signals['lma']=data["WIKI/"+ticker+' - Close'].rolling(20).mean()

    signals[['sma','lma']].plot(ax=ax1,lw=2.)
    plt.show()
