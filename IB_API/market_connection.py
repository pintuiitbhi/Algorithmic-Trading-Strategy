from ibapi.wrapper import EWrapper
from ibapi.client import EClient
from ibapi.contract import *
from ibapi.order import Order
from ibapi.common import *
# from ibapi.connection import Connection

from IB_API.trader import *
from quandlData.Qdata import *

# from Strategies.show_positions import *
from Strategies.moving_average_strategy import *

import time
import datetime
import pytz
import pandas as pd
import os

cwd = os.getcwd() #current working directory


class TestWrapper(EWrapper):
    def __init__(self):
        EWrapper.__init__(self)

class TestClient(EClient):
    def __init__(self, wrapper):
        EClient.__init__(self, wrapper)

class TestApp(TestWrapper, TestClient):
    #contracts.csv
    stockList = pd.read_csv(os.path.join(cwd, 'database/contracts.csv'))


    def __init__(self,ipaddress, portid, clientid):
        TestWrapper.__init__(self)
        TestClient.__init__(self, wrapper=self)
        self.nextValidOrderId = int(time.mktime(datetime.datetime.now().timetuple()))
        self.connect(ipaddress, portid, clientid)

        self.showTimeZone = pytz.timezone('Asia/Kolkata')

    def retStockList(self):
        return self.stockList

    def error(self, reqId:TickerId, errorCode:int, errorString:str):
        print("Error: "," ",reqId," ",errorCode," ",errorString)

def main():
    print("Running market connection")

    #TODO
    # disconnect=Connection('127.0.0.1',7497)
    # if ~disconnect.isConnected():
    #     disconnect.disconnect()
    #     print("disconnectedddddddd")

    app = TestApp("127.0.0.1",7497,999)
    if app.isConnected():
        print("serverVersion:%s connectionTime:%s" % (app.serverVersion(),
                                                  app.twsConnectionTime()))
    else:
        print("Error : Not connected")
    contracts = app.retStockList()

    print(contracts.head()) #contracts.csv

    counter=0
    for i in stocks:
        print("-------------------------------------")
        print("Doing Trading for ",tickers[counter])
        print(i)
        contract = create_contract(i) #create contract
        uniqueId = int(time.mktime(datetime.datetime.now().timetuple())) #finding unique id using datetime
        print("Contract Created")
    # app.reqMarketDataType(MarketDataTypeEnum.FROZEN)

        print("Plotting moving average for....",tickers[counter])

        end_date=str((datetime.datetime.now() - datetime.timedelta(days=1)).date())
        plot_historical_data(tickers[counter],'2018-01-01',end_date) #Plotting moving average of all time period

        roundtrips=pd.read_csv(os.path.join(cwd,'database/roundtrips.csv'))

        print("STRATEGY executing for..",tickers[counter])
        strategy(app,i,tickers[counter],short_window,long_window,end_date)
        counter+=1

    print("Trading Completed for Today")

    app.run()
    app.disconnect()

if __name__ == "__main__":
    main()
