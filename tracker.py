import requests
import re
from bs4 import BeautifulSoup

source = "https://news.google.com/covid19/map?hl=en-PH&gl=PH&ceid=PH:en"
request = requests.get(source)
content = request.content

soup = BeautifulSoup(content,"html.parser")

confirmed = soup.find("div", {"class": "fNm5wd qs41qe", "class": "UvMayb"})

recovered = (soup.find("div", {"class": "fNm5wd gZvxhb"})).text
recovered = ''.join(filter(lambda i: i.isalpha()==False, recovered))

deaths = (soup.find("div", {"class": "fNm5wd ckqIZ"})).text
deaths = ''.join(filter(lambda i: i.isalpha()==False, deaths))
updated = soup.find("time", {"class": "vBLAZ Yt6XT"})

print("Coronavirus(COVID-19) Cases Worldwide")

print("Confirmed Cases: {0}".format(confirmed.text))
print("Recovered Cases: {0}".format(recovered))
print("Death Cases: {0}".format(deaths))
print("Source: {0}".format(source))
print(updated.text)
