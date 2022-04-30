from pandas.core.arrays.integer import safe_cast
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time,os,datetime

def getFinancialInformation(symbol):
    # url = r"https://finance.yahoo.com/quote/%5EGSPC?p=%5EGSPC"
    url = "https://finance.yahoo.com/quote/"+symbol+"?p="+symbol

    response = requests.get(url)

    t = response.text

    soup = BeautifulSoup(t,features="html.parser")
 
    trs = soup.find_all("tr")

    finaltag = "Avg. Volume"
    
    # print(trs[0].contents[0].text)
    # print(trs[0].contents[1].text)

    names = []
    values = []

    namVal = {}


    for i in range(len(trs)):
        for j in range(len(trs[i].contents)):
            if j==0:
                try:
                    name = trs[i].contents[j].text
                    names.append(name)
                except:
                    continue
            if j==1:
                try:
                    value = trs[i].contents[j].text
                    values.append(value)
                except:
                    continue
        namVal[name]=value
        if name==finaltag:
            break
    print("working")
    return names,values
   
    # print(names)
    # print(values)
    # print(namVal)


def getCompanyList():
    wikiurl = r"https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

    response = requests.get(wikiurl)

    t = response.text

    soup = BeautifulSoup(t,features="html.parser")
    tickerSymbol=[]
    finaltag = "ZTS"
    tbody = soup.find_all("tbody")

    


    for i in range(len(tbody[0].contents)):
        if i<2:
            continue
        if i%2 != 0:
            continue
        symbol = tbody[0].contents[i].contents[1].text
        tickerSymbol.append(symbol.strip("\n"))
        if len(tickerSymbol)== 505:
            break

    # print(tickerSymbol)
    print("working2")
    return tickerSymbol

while True:
    start = time.time()
    waittime = 150
    data = {"symbol":[],
            "metric":[],
            "value":[],
            "time":[]
    }

    cpynames = getCompanyList()
    for symbol in cpynames:
        names,values = getFinancialInformation(symbol)
        collectedTime = datetime.datetime.now().timestamp()

        for i in range(len(names)):
            data["symbol"].append(symbol)
            data["metric"].append(names[i])
            data["value"].append(values[i])
            data['time'].append(collectedTime)

    df = pd.DataFrame(data)
    savePath =  "FinancialData.csv"    
    if os.path.isfile(savePath):
        df.to_csv(savePath,mode="a",header=False,columns=["symbol","metric","value","time"])
    else:
        df.to_csv(savePath,columns=["symbol","metric","value","time"])
    # df.to_csv("FinacialData.csv")

    timeDiff = time.time() - start
    if waittime-timeDiff>0:
        time.sleep(waittime-timeDiff)
