import requests
from bs4 import BeautifulSoup

url = "http://www.atmovies.com.tw/movie/next/"
Data = requests.get(url)
Data.encoding = "utf-8"
#print(Data.text)
sp = BeautifulSoup(Data.text, "html.parser")
result=sp.select(".filmListAllX li")

for x in result:
	print("片名:" + x.find("img").get("alt"))
	print("電影介紹:http://www.atmovies.com.tw" + x.find("a").get("href"))
	print("電影海報:" + x.find("img").get("src").replace(" ", ""))
	print(x.find(class_="runtime").text("上映日期：", ""))
	print()