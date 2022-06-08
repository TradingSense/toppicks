import streamlit as st
import stocker
from yahoo_fin import stock_info as si
hotstocks =['TSLA','AMZN','BA','COST']




col1,col2,col3,col4 = st.columns(4)


tsla = stocker.predict.tomorrow('tsla')
tslaacc = tsla[1]
tslafor= tsla[0]

amzn = stocker.predict.tomorrow('amzn')
amznacc = amzn[1]
amznfor= amzn[0]

amznlive= si.get_live_price('amzn')

tslalive= si.get_live_price('tsla')

tsladelt = tslafor - tslalive 
tsladelt = round(tsladelt,2)


amzndelt = amznfor - amznlive 
amzndelt = round(amzndelt,2)
col3.metric('$TSLA 7 Day Forecast',tslafor,delta=tsladelt)
col4.metric('Backtest Accuracy',str(100-tslaacc)+'%')
col3.metric('$AMZN 7 Day Forecast ',amznfor,delta = amzndelt)
col4.metric('Backtest Accuracy ',str(100-amznacc)+'%')
col1.header('TSLA')
col1.header('AMZN')
col2.metric('TSLA Live Price',round(tslalive,2))
col2.metric('AMZN Live Price',round(amznlive,2))

 
