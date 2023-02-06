import requests
import pandas as pd
from dotenv import load_dotenv
import os
from loguru import logger

def get_dashboard_data():
    target_dic={"tw_index":"^TWII",
    "0050":"0050.TW",
    "0051":"0051.TW",
    "Dow Jones Industrial Average":"^DJI",
    "S&P 500":"^GSPC",
    "NASDAQ Composite":"^IXIC",
    "BTC/USDT":"BTC-USD",
    "ETH/USDT":"ETH-USD",
    "BNB/USDT":"BNB-USD"}
    symbol_str=""
    for key,value in target_dic.items():
        symbol_str+=f"{value},"
        
    print(symbol_str[0:-1])

    url_quote = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"
    querystring_quote = {"region":"US","symbols":symbol_str[0:-1]}
    headers = {
	    "X-RapidAPI-Key": "9662692fbfmsh198d40754c15840p1411c3jsn2113b55048e9",
	    "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }
    response_quote = requests.request("GET", url_quote, headers=headers, params=querystring_quote)

    url_chart = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-spark"
    querystring_chart = {"interval":"5","range":"1d","symbols":symbol_str[0:-1]}
    headers = {
	    "X-RapidAPI-Key": "9662692fbfmsh198d40754c15840p1411c3jsn2113b55048e9",
	    "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }
    response_quote = requests.request("GET", url_chart, headers=headers, params=querystring_chart)

    dashboard_list=[]
    for key,value in target_dic.items():
        index = list(target_dic.values()).index(value)
        response_quote.json()["quoteResponse"]["result"][index]
        dashboard_list.append({
            "target":key,
            "currency":response_quote.json()["quoteResponse"]["result"][index]["currency"],
            "last_time":response_quote.json()["quoteResponse"]["result"][index]["regularMarketTime"],
            "last_price":response_quote.json()["quoteResponse"]["result"][index]["regularMarketPrice"],
            "daily_high":response_quote.json()["quoteResponse"]["result"][index]["regularMarketDayHigh"],
            "daily_low":response_quote.json()["quoteResponse"]["result"][index]["regularMarketDayLow"],
            "daily_open":response_quote.json()["quoteResponse"]["result"][index]["regularMarketOpen"],
            "previous_close":response_quote.json()["quoteResponse"]["result"][index]["regularMarketPreviousClose"],

        })
        print(dashboard_list)
        break
if __name__ == '__main__':
    get_dashboard_data()