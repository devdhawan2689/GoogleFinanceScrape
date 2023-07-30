from bs4 import BeautifulSoup
import requests 
import pprint
import pandas as pd
import numpy as np
import matplotlib as mp 

stock_list = pd.read_csv('List-Of-Stocks.csv')
# stock_list

def getPrice(stockName):
     # Website URL
    URL = 'https://www.google.com/finance/quote/' + stockName +':NSE?hl=en'

    # class list set
    class_list = set()

    # Page content from Website URL
    page = requests.get( URL )

    # parse html content
    soup = BeautifulSoup( page.content , 'html.parser') 
    # pprint.pprint(soup)
    
    price = soup.findAll("div", class_="YMlKec fxKbKc") 
    output = price[0].string 

    return output 

def getAllPrice(printOutput):
    output = []
    for stockName in stock_list['Symbol']:
        # Website URL
        URL = 'https://www.google.com/finance/quote/' + stockName +':NSE?hl=en'

        # class list set
        class_list = set()

        # Page content from Website URL
        page = requests.get( URL )

        # parse html content
        soup = BeautifulSoup( page.content , 'html.parser') 
        # pprint.pprint(soup)
        
        price = soup.findAll("div", class_="YMlKec fxKbKc") 
        appendVal = stockName + " - " + price[0].string

        if printOutput == True:
            print(appendVal)

        output.append(appendVal)
        
    return output

def searchSymbol(stockName):
    companyName = stock_list[stock_list['Symbol'] == stockName]
    print(companyName['Company Name'].values[0]) 

def getCompanyStats(stockName):
     # Website URL
    URL = 'https://www.google.com/finance/quote/' + stockName +':NSE?hl=en'

    # class list set
    class_list = set()

    # Page content from Website URL
    page = requests.get( URL )

    # parse html content
    soup = BeautifulSoup( page.content , 'html.parser') 
    # pprint.pprint(soup)
    
    price = soup.findAll("div", class_="P6K39c") 
    
    columns = ["PREVIOUS CLOSE", "DAY range", "YEAR RANGE", "MARKET CAP", "P/E RATIO", "DIVIDEND YIELD", "PRIMARY EXCHANGE"]
    values = []

    for index in range(len(columns)):
        values.append(price[index].string)
    
    companyStats = pd.DataFrame(list(zip(columns, values)),columns = ["Stats", "Values"])

    return companyStats

def getPreviousClose(stockName):
     # Website URL
    URL = 'https://www.google.com/finance/quote/' + stockName +':NSE?hl=en'

    # class list set
    class_list = set()

    # Page content from Website URL
    page = requests.get( URL )

    # parse html content
    soup = BeautifulSoup( page.content , 'html.parser') 
    # pprint.pprint(soup)
    
    price = soup.findAll("div", class_="P6K39c") 
    output = price[0].string 

    return output 

def getDayRange(stockName):
     # Website URL
    URL = 'https://www.google.com/finance/quote/' + stockName +':NSE?hl=en'

    # class list set
    class_list = set()

    # Page content from Website URL
    page = requests.get( URL )

    # parse html content
    soup = BeautifulSoup( page.content , 'html.parser') 
    # pprint.pprint(soup)
    
    price = soup.findAll("div", class_="P6K39c") 
    output = price[1].string 

    return output 

def getYearRange(stockName):
     # Website URL
    URL = 'https://www.google.com/finance/quote/' + stockName +':NSE?hl=en'

    # class list set
    class_list = set()

    # Page content from Website URL
    page = requests.get( URL )

    # parse html content
    soup = BeautifulSoup( page.content , 'html.parser') 
    # pprint.pprint(soup)
    
    price = soup.findAll("div", class_="P6K39c") 
    output = price[2].string 

    return output 

def getMarketCap(stockName):
     # Website URL
    URL = 'https://www.google.com/finance/quote/' + stockName +':NSE?hl=en'

    # class list set
    class_list = set()

    # Page content from Website URL
    page = requests.get( URL )

    # parse html content
    soup = BeautifulSoup( page.content , 'html.parser') 
    # pprint.pprint(soup)
    
    price = soup.findAll("div", class_="P6K39c") 
    output = price[3].string 

    return output 

def getPERatio(stockName):
     # Website URL
    URL = 'https://www.google.com/finance/quote/' + stockName +':NSE?hl=en'

    # class list set
    class_list = set()

    # Page content from Website URL
    page = requests.get( URL )

    # parse html content
    soup = BeautifulSoup( page.content , 'html.parser') 
    # pprint.pprint(soup)
    
    price = soup.findAll("div", class_="P6K39c") 
    output = price[4].string 

    return output 

def getDividendYield(stockName):
     # Website URL
    URL = 'https://www.google.com/finance/quote/' + stockName +':NSE?hl=en'

    # class list set
    class_list = set()

    # Page content from Website URL
    page = requests.get( URL )

    # parse html content
    soup = BeautifulSoup( page.content , 'html.parser') 
    # pprint.pprint(soup)
    
    price = soup.findAll("div", class_="P6K39c") 
    output = price[5].string 

    return output 

def getPrimaryExchange(stockName):
     # Website URL
    URL = 'https://www.google.com/finance/quote/' + stockName +':NSE?hl=en'

    # class list set
    class_list = set()

    # Page content from Website URL
    page = requests.get( URL )

    # parse html content
    soup = BeautifulSoup( page.content , 'html.parser') 
    # pprint.pprint(soup)
    
    price = soup.findAll("div", class_="P6K39c") 
    output = price[6].string 

    return output 

