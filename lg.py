import requests as re
import pandas
from bs4 import BeautifulSoup

just=re.get('https://www.vijaysales.com/tv-and-entertainment/televisions/brand/buy-lg-televisions')
soop=BeautifulSoup(just.content,'html.parser')
name=soop.find_all('h2',class_="BcktPrdNm_")
newnames=[]
for i in name[1:7]:
	f=i.get_text()
	newnames.append(f)
#print(newnames)

price=soop.find_all('span',class_="Prdvsprc_")
newprices=[]
for i in price[1:7]:
	f=i.get_text()
	newprices.append(f)
#print(newprices)
emidetails=soop.find_all('div',class_="BcktPrdemi h54")
emi2=[]
for i in emidetails[1:7]:
	f=i.get_text()
	emi2.append(f)
#print(emi2)


exchangedetails=soop.find_all('div',class_="ofrPrd")
exchange=[]
for i in exchangedetails[1:7]:
	f=i.get_text()
	exchange.append(f)
#print(exchange)

producturls=soop.find_all('a',id="pdpId_")
product=[]
for i in producturls[1:7]:
	f=i['href']
	product.append(f)
#print(product)

data={"name":newnames,"price":newprices,"emi":emi2,"exchangedetails":exchange,"urls":product}
df=pandas.DataFrame(data)
df.to_csv("lg.csv")