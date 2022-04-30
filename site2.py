import requests
from bs4 import BeautifulSoup


url = r"https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

response = requests.get(url)

# t = response.text

# soup = BeautifulSoup(t,features="html.parser")

# finaltag = "ZTS"
# trs = soup.find_all("tr")

# names = []



# for i in range(len(trs)):
#     name = (trs[i].contents[1].text)
#     name = name.strip("\n")
#     if name == finaltag:
#         break
#     names.append(name)
# names.append(finaltag)
    
# # print(trs[2].contents[1].text)
# print(names)
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

print(tickerSymbol)