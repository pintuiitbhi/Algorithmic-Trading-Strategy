# -*- coding: utf-8 -*-
from IB_API.market_connection import *
from IB_API.trader import *
from quandlData.Qdata import *
import time
import pandas as pd
import matplotlib.pyplot as plt
import os

def strategy(app,stock,tickers ,short_window,long_window,new_date):

    # sTime = app.currentTime(time.time()) #Current
    cwd= os.getcwd()

    #Opening all Database to read
    print("Database opened..")
    contracts= pd.read_csv(os.path.join(cwd,'database/contracts.csv'))
    signal_db = pd.read_csv(os.path.join(cwd,'database/signal_db.csv'))

    roundtrips = pd.read_csv(os.path.join(cwd,'database/roundtrips.csv'))

    print("Fetching Historical Data of ",tickers)
    data=fetch_historical_data(tickers,new_date) #backtest
    print("Fetcheded...",tickers)
    print(data.tail())

    print("Calculating Moving Average ...")
    SignalColumns = ['sma','lma','signals']
    signal_db = pd.DataFrame(columns=SignalColumns)
    signal_db['signals']=0
    signal_db.to_csv(os.path.join(cwd,'database/signal_db.csv'), index=False, header = True)

    signal_db['sma']=data['Close'].rolling(5).mean()
    signal_db['lma']=data['Close'].rolling(20).mean()
    mv5=data['Close'].rolling(5).mean().iloc[-1]
    mv20=data['Close'].rolling(20).mean().iloc[-1]
    print("Small MA: ",mv5)
    print("Large MA: ",mv20)
    if mv5>mv20:
        print("Small moving average is GREATER")
    else:
        print("Large moving average is GREATER")

    # app.reqMarketDataType(4)
    # current_price = app.reqMktData(uniqueId,contract , "", False, False, [])     #TODO
    # print(current_price)

    new_date=str(datetime.datetime.now().date()) #current_date
    data=fetch_historical_data(tickers, new_date)

    current_price = data['Open'][-1]
    print("Current Price of Stock: ",current_price)
    # current_positions=5
    # cash=10000

    # cash = roundtrips['balance']

    index=contracts[contracts['Symbol']==str(stock.iloc[0]['Symbol'])].index.item() #integer
    current_positions =contracts.iloc[index]['Flag'] #number of shares
    cash = contracts.iloc[index]['Cash']
    number_of_shares = int(cash/current_price)
    print("Cash: ", cash)
    print("number_of_shares: ", number_of_shares)
    print("Current Positions: ", current_positions)
    # buy=0#backtest
    trade=0
    if mv5>mv20 and current_positions == 0 and number_of_shares!=0:
        #BUY
        contract = create_contract(stock)
        uniqueId = int(time.mktime(datetime.datetime.now().timetuple()))

        order = create_order("BUY","LMT",number_of_shares,current_price,True)
        app.placeOrder(uniqueId,contract,order)
        #Update positions
        t = contracts.iloc[index]['Flag']+number_of_shares
        contracts.iloc[index, contracts.columns.get_loc('Flag')] = t

        #Update cash balance
        # t = contracts.iloc[index]['Cash']+number_of_shares
        contracts.iloc[index, contracts.columns.get_loc('Cash')] = 0

        print("Buying done ")
        trade=1

        dict = pd.Series([tickers,data.index[-1],1,cash], index=['instrument','trading_date', 'signal', 'buying'])
        print("Dictionary :", dict)
        roundtrips=roundtrips.append(dict,ignore_index=True)
        print("Roundtrips :",roundtrips)
        # app.order_status_monitor(orderId, target_status='Filled')#TODO
    elif mv5<mv20 and current_positions != 0:
        # SELL
        contract = create_contract(stock)
        uniqueId = int(time.mktime(datetime.datetime.now().timetuple()))

        order = create_order("SELL","LMT",current_positions,current_price,True)
        app.placeOrder(uniqueId,contract,order)

        contracts.iloc[index, contracts.columns.get_loc('Flag')] = 0 #sold all shares

        print("Selling done")
        trade=0

        Current_balance=current_positions*current_price
        contracts.iloc[index, contracts.columns.get_loc('Cash')] = Current_balance
        dict = pd.Series([tickers,data.index[-1],-1,-Current_balance], index=['instrument','trading_date', 'signal', 'buying'])
        print("Dictionar: ",dict)
        roundtrips=roundtrips.append(dict,ignore_index=True)
        print("Roundtrips :",roundtrips)

    if trade==0:
        print("No Trading...")
    else:
        print("Trading Done")

    print("Saving Database...")

    signal_db.to_csv(os.path.join(cwd,'database/signal_db.csv'), index=False, header = True)
    contracts.to_csv(os.path.join(cwd,'database/contracts.csv'), index=False, header = True)
    roundtrips.to_csv(os.path.join(cwd,'database/roundtrips.csv'), index=False, header = True)

    # print("OrderId ",uid)
    print("Strategy execution completed :",tickers)


# if __name__ == '__main__':
#     setup()
#     loop()
