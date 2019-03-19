# -*- coding: utf-8 -*-
#Run on Linux platform
#To run on windows just change the '/' to '\' in database path wherever used

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from IB_API.market_connection import *
from sys import exit
import os

from IB_API.trader import *

short_window = 5 #short moving average
long_window = 20 #long moving average

tickers=['GOOG','FB'] #ticker

stocks = symbols("GOOG","FB")
# print(stocks)

print(".....RUN_ME.... Finished")

print("Calling market_connection.py...")

with open(os.path.join(os.getcwd(), 'IB_API', 'market_connection.py')) as f:
    script = f.read()
exec(script)
