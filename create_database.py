import pandas as pd
import os


cwd = os.getcwd() #current working directory

def createDatabase():
    #PORTFOLIO Database
    cwd= os.getcwd()
    # PortfolioColumns = ['Stock','Capital_used','Cash', 'Pnl', 'Portfolio_value', 'Positions_value', 'Returns', 'Starting_cash', 'Start_date']
    # portfolio_db = pd.DataFrame(columns=PortfolioColumns)
    # portfolio_db.to_csv(os.path.join(cwd,'database/portfolio_db.csv'), index=False,header = True)

    #Order Database
    # OrderColumns =['OrderId','Submitted_date','ContId','Action','Total_quantity','Account','Status','Filled','Remaining']
    # order_db = pd.DataFrame(columns=OrderColumns)
    # order_db.to_csv(os.path.join(cwd,'database/order_db.csv'), index=False,header = True)

    #Trade Signal Database
    SignalColumns = ['sma','lma','signals']
    signal_db = pd.DataFrame(columns=SignalColumns)
    signal_db['signals']=0
    signal_db.to_csv(os.path.join(cwd,'database/signal_db.csv'), index=False, header = True)

    contracts= pd.read_csv(os.path.join(cwd,'database/contracts.csv'))
    # contracts.set_index("Instrument",inplace=True)
    contracts['Flag']=0 #initialize positions
    contracts['Cash']=100000 #add cash in account
    contracts.to_csv(os.path.join(cwd,'database/contracts.csv'), index=False, header = True)

    columns=['instrument','trading_date','signal','buying']
    roundtrips = pd.DataFrame(columns=columns)
    roundtrips.to_csv(os.path.join(cwd,'database/roundtrips.csv'), index=False, header = True)

def initialize():
    createDatabase()
    print("Database created")


if __name__ == "__main__":

    initialize()
