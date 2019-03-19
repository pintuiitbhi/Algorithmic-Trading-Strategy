# Algorithmic-Trading-Strategy

>>>>>>>>>>>>>>>>>>>>>>>>>>>>GROUP-2<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Members:
Pintu Kumar
Devansh Bajpai
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

We have used the official IB API from the IB for this project and for doing backtest
we wrote our own code in python to backtest it.

1. The project is build on Linux Ubuntu 16.04 LTS using Python 3.6 environment
2. Interactive Broker Latest TWS is used for connection with IB API.

 #########################################################################
 ..................Connection Settings in TWS and Python program..........
 We have used Demo account of IB. Since only one user can login at a time in IB. So use this setting in TWS api
 settings.

 Host: 127.0.0.1
 Socket Port : 7497
 Master Client Id : 999

      Use the above settings in python and TWS for establishing connection.
 ########################################################################


#########################################################################
...................Automating the Trade..................................
In order to automate the trade such that trading is performed daily in morning time,
we scheduled the file "RUN_ME.py" in Ubuntu in "crontab file". The file "RUN_ME.py"
run daily in morning after market opens (after 1 minute).

To schedule the program such that trading is performed only from Monday to Friday in morning, use the following
crontab command in terminal.

"15 9 * * 1-5 python3 RUN_ME.py"
This command will do trading at 9:15am from Monday to Friday

#########################################################################


#########################################################################
.....................Steps to execute the Project..........................
After performing above settings in TWS api settings tab
1. Run the file "create_database.py" .
    NOTE:- if you are running on windows then change the path symbol from "/" to "\".
            in file "create_database.py" and "moving_average_strategy.py"

            Only once we need to run "create_database.py" . Not everyday.

2. Then run "RUN_ME.py".


#########################################################################

#########################################################################
 ....................Structure of Project Folder "trading02"..............

(a.) The file "RUN_ME.py" is to control the configuration of trading. Like User can put enter the moving average period
      they want to calculate whether 10 days, 20 days, 50 days etc in variable "short_window" and "long_window"

      Trader can also define the stock in which they want to trade in list "tickers" and the function "symbols()" in same order.

      The last three lines of "RUN_ME.py" calls the module "market_connection.py" from folder "IB_API"

(b.) The file "create_database.py" creates the required database to store the results during trading for each day.
        It should be run ONLY once before running "RUN_ME.py".


 1. Folder "IB_API" contains the file "market_connection.py" and "trader.py"

 >>> File "market_connection.py" contains the class to create connection between the TWS and Python program
      and object "app".
      It is the main program which call the "strategy()" function from file "moving_average_strategy.py" to execute the
      strategy.

>>> File "trader.py"  contains functions to create order, create contract and convert given ticker to stocks which was
    mapped from the "contracts.csv" file.

2.  Folder "quandlData" contains the module to fetch historical data for given "instrument" and plot the moving Average for
    given "stock"
      Functions included in the module are : fetch_historical_data() and plot_historical_data()

3.  Folder "Strategies" has the module "moving_average_strategy.py" related to Calculating moving average and placing order on IB.
    This module has function "strategy()" which calculates small moving average and large moving average.

4. The folder "database" stores the "contracts.csv" ,  "signal_db.csv" ,"roundtrips.csv" and "historicaldat.csv"
  >>> contracts.csv : it has all stocks detail like symbol, currency , expiry, exchange etc.
  >>> signal_db.csv : it store the small moving average and large moving average for Plotting sma and lma
  >>> roundtrips.csv : it keep record of each trade like trading date, instrument, signal (-1 for Selling and 1 for buying), and
      buying (column for storing buying or selling price, negative value for selling)
  >>> historicaldat.csv : it stores the fetched historical data from quandl website.
###################################################################################################

###################################################################################################
......................................Backtest....................................................
In order to do the backtest we download historical data from quandl for a year and simulated on it
for one year and executed the order on IB.

"Backtrader" does not directly support the code written using "IB API". We were facing problem in backtesting.
So, we write our own code to backtest the strategy.

"Backtrader" is used for program which is written using IBPy library which uses Java IB API indirectly .
####################################################################################################

####################################################################################################
................................Work Remaining to do in the Project.................................
1.Getting live portfolio and order details .
2.Order status monitoring.
3.Requesiting live stock price.
#####################################################################################################
