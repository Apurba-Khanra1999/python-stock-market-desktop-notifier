import datetime
import time
from plyer import notification
import yfinance as yf

apple = yf.Ticker("AAPL")
data = apple.info

while True:
    notification.notify(
        title = "Stock Data - AAPL" .format(datetime.date.today()),
        message = "Current Price - {cp} \n Day High - {dh}\n Day Low - {dl}\n".format(
            cp = data["currentPrice"],
            dh = data["dayHigh"],
            dl = data["dayLow"]
        ),
        app_icon = "notif.ico",
        timeout = 3
    )
    time.sleep(10)