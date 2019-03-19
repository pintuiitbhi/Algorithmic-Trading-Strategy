import pandas as pd
from ibapi.contract import *
from ibapi.order import Order
import os

def instr_to_security(stockList,s1):
    tmp_stockList = stockList[(stockList['Instrument'] == s1)]
    # print(tmp_stockList.shape)
    if tmp_stockList.shape[0]==1:
        return tmp_stockList
    else:
        print ('%s is missing.' % (s1))
        print ('Please add this info in contracts.csv')
        exit()

def symbol(str_instr):
    cwd=os.getcwd()
    stockList = pd.read_csv(os.path.join(cwd, 'database/contracts.csv'))

    # print(stockList.head())
    security = instr_to_security(stockList,str_instr)
    print(security)
    return security


def symbols( *args):
    ls = []
    for item in args:
        ls.append(symbol(item))
    return ls

def create_contract(security):
    c = Contract()
    print("Security Symbol", str(security.iloc[0]['Symbol']))
    c.symbol = str(security.iloc[0]['Symbol'])

    c.secType = str(security.iloc[0]['Type'])
    # c.expiry = row['Expiry']
    c.exchange = str(security.iloc[0]['Exchange'])
    c.currency = str(security.iloc[0]['Currency'])
    return c

#create order
def create_order(action,secType,quantity,price,transmit):
    order = Order()
    order.action = action
    order.orderType = secType
    order.totalQuantity = quantity
    order.lmtPrice = price
    order.Transmit= transmit
    return order
