import datetime
import time
from plyer import notification
import yfinance as yf
import streamlit as st

apple = yf.Ticker("AAPL")
print(apple.info)
st.write(apple.info)