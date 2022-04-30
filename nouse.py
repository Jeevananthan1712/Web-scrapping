import requests
from bs4 import BeautifulSoup
url = r"https://finance.yahoo.com/quote/%5EGSPC?p=%5EGSPC"


response = requests.get(url)

t = response.text

soup = BeautifulSoup(t,features="html.parser")

trs = soup.find_all("tr")

finaltag = "Avg. Volume"
 
print(trs[0].contents[0].text)
print(trs[0].contents[1].text)

names = []
values = []

namVal = {}


for i in range(len(trs)):
    for j in range(len(trs[i].contents)):
        if j==0:
            name = trs[i].contents[j].text
            names.append(name)
        if j==1:
            value = trs[i].contents[j].text
            values.append(value)
            namVal[name]=value
        if name==finaltag:
            break
print(names)
print(values)
print(namVal)
