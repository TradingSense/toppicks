
import streamlit as st
st.set_page_config(layout='wide')
import pandas as pd
import matplotlib.pyplot as plt
from stockstats import StockDataFrame
import yfinance as yf
from datetime import *
from datetime import date
from datetime import timedelta
import time
import dataframe_image as dfi
from yahoo_fin import stock_info as si
import stocker
import re
import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs
import pandas_datareader.data as web
import ssl 
import requests
from urllib import request

col1 ,col2,col3 = st.columns(3)

set =['TSLA','AMZN','BA','COST','JOBY','F','GM','XOM','NVDA','AMD','AAPL','SNAP','TWTR','DVAX','BAC','MCD','GE']
num = -1
z=1
while  z == 1:
    
    num = num +1
    if num == 17:
        num = -1
    ticker = set[num]
    
    today = date.today()
    yesterday = today - timedelta(days = 1)
    start = '2022-01-01'      
    end = datetime.today().strftime('%Y-%m-%d')
    customdata = yf.download(ticker,start,end)
    customframe = StockDataFrame.retype(customdata)
    stock = customframe
    custommfi = stock.get('mfi')[yesterday.strftime('%Y-%m-%d')].round(2)*100
    customwr = stock.get('wr')[yesterday.strftime('%Y-%m-%d')].round(2)

    h = stocker.predict.tomorrow(ticker)[0]
    live = si.get_live_price(ticker)

    day = 1
    weekday = datetime.today().weekday()
    
    if weekday == 0:
        day = 3
    elif weekday == 6:
        day = 2
    else:
        day = 1
    if custommfi < 20:
        customstate = 'Oversold/Undervalued'
    elif custommfi > 80:
        customstate = 'Overbought/Overvalued'
    else:
        customstate = 'Normal '

    if customwr < -80:
        customheight = 'Lower Than Normal'
    elif customwr > -20:
        customheight = 'Higher Than Normal'
    else:
        customheight = 'Normal'
    if customheight == 'Lower Than Normal' and customstate == 'Oversold/Undervalued' and h >= live + 5:
        recc = 'STRONG BUY'
    elif customheight == 'Higher Than Normal' and customstate == 'Overbought/Overvalued':
        recc = 'SELL'
    elif customheight == 'Lower Than Normal' and customstate == 'Normal ':
        recc = 'BUY'
    elif customheight == 'Higher Than Normal' and customstate == 'Normal ' and h >= live + 5:
        recc = 'HOLD'
    elif h >= live + 50:
        recc = 'LTSM BUY'
        
    else:
        recc='HOLD'
    old = customdata['close'].tail()
    old1 = old[2]
    pastprice = old1 - live
    pastprice = round(pastprice,2)    
    difference = h - live
    difference = round(difference,2)
    if difference > 0:
        direction = 'Gain'
    elif difference < 0:
        direction ='Loss'
    col1.header(ticker)
    col2.metric('Signal',recc)
    col3.metric('Live Price',round(live,2),delta = str(pastprice)+' 24Hour')
    time.sleep(10)


