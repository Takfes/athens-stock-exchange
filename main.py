from tqdm import tqdm
import logging
import os, json, sys, requests, time, calendar
import pandas as pd
import numpy as np
from datetime import datetime
import yfinance as yf


data = pd.read_csv('athex_20220107.txt')
data.columns = [x.replace('<','').replace('>','') for x in data.columns]
data.sort_values(by='ticker',inplace=True)
tickers = [x+".AT" for x in data.ticker.unique().tolist()]


history_list = []
failed = []
info_list = []

financials_list = []
quarterly_financials_list = []

balance_sheet_list = []
quarterly_balance_sheet_list = []

earnings_list = []
quarterly_earnings_list = []



for tic in tqdm(tickers):
    
    # tic = tickers[22] # BELA.AT
    temp = yf.Ticker(tic)
    
    # history_list
    try:
        foo = temp.history(period='max').assign(ticker = tic)
        # foo = temp.history(start="2017-01-01", end="2017-04-30")
        if not foo.empty:
            history_list.append(foo)
        else :
            failed.append(tic)    
    except:
        failed.append(tic)
    
    # info_list
    try :
        foo = pd.DataFrame().from_dict(yf.info,orient='index').T.assign(ticker = tic)
        info_list.append(foo)
    except:
        pass
    
    # financials_list
    try :
        foo = temp.financials.assign(ticker = tic)
        financials_list.append(foo)
    except:
        pass
    
    # quarterly_financials_list
    try :
        foo = temp.quarterly_financials.assign(ticker = tic)
        quarterly_financials_list.append(foo)
    except:
        pass
    
    # balance_sheet_list
    try :
        foo = temp.balance_sheet.assign(ticker = tic)
        balance_sheet_list.append(foo)
    except:
        pass
    
    # quarterly_balance_sheet_list
    try :
        foo = temp.quarterly_balance_sheet.assign(ticker = tic)
        quarterly_balance_sheet_list.append(foo)
    except:
        pass
    
    # earnings_list
    try :
        foo = temp.earnings.assign(ticker = tic)
        earnings_list.append(foo)
    except:
        pass
    
    # quarterly_earnings_list
    try :
        foo = temp.quarterly_earnings.assign(ticker = tic)
        quarterly_earnings_list.append(foo)
    except:
        pass
    
    
len(history_list)
len(failed)

df = pd.concat(history_list)
len(df.ticker.unique().tolist())
    
  
# temp.info
# pd.DataFrame().from_dict(temp.info,orient='index').T
# pd.DataFrame().from_dict(temp.info)

# temp = yf.Ticker('FOYRK.AT')

# temp.info
# temp.financials
# temp.quarterly_financials
# temp.balance_sheet
# temp.quarterly_balance_sheet
# temp.earnings
# temp.quarterly_earnings

# temp.dividends
# temp.calendar
# temp.recommendations
# temp.major_holders
# temp.splits
# temp.actions



