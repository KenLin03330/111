import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

from flask import Flask, render_template, request
from datetime import datetime, timezone, timedelta

import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>浚承Python網頁1121</h1>"
    homepage += "<a href=/mis>MIS</a><br>"
    homepage += "<a href=/today>顯示日期時間</a><br>"
    homepage += "<a href=/welcome?nick=林浚承>傳送使用者暱稱</a><br>"
    homepage += "<a href=/sweetpotato>浚承簡介網頁</a><br>"
    homepage += "<a href=/account>輸入帳密傳值</a><br>"
    homepage += "<a href=/read>人選之人演員查詢</a><br><br>"
    homepage += "<a href=/books>精選圖書列表</a><br>"
    homepage += "<a href=/query>書名查詢</a><br><br>"
    homepage += "<a href=/spider>網路爬蟲抓取子青老師課程</a><br>"
    homepage += "<a href=/movie>讀取開眼電影即將上映影片</a><br>"

    return homepage


@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"
@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html", datetime = str(now))
@app.route("/sweetpotato")
def sweetpotato():
    return render_template("sweetpotato.html")
@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)
@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")

@app.route("/read")
def read():
    Result = ""
    db = firestore.client()
    collection_ref = db.collection("人選之人─造浪者")    
    docs = collection_ref.get()    
    for doc in docs: 
        X = doc.to_dict()        
        Result += "演員：{},劇中角色是{},出生於{}".format(X["name"], X["role"], X["birth"]) + "<br>"    
    return Result

@app.route("/books")
def books():
    Result = ""
    db = firestore.client()
    collection_ref = db.collection("圖書精選")    
    docs = collection_ref.get()
    for doc in docs:
        bk = doc.to_dict()
        Result += "書名：<a href=" + bk["url"] + ">" + bk["title"] + "</a><br>"
        Result += "作者：" + bk["author"] + "<br>"
        Result += str(bk["anniversary"]) + "週年紀念版<br>"
        Result += "<img src=" + bk["cover"] + "> </img><br><br>"
    return Result

@app.route("/query", methods=["GET", "POST"])
def query():
    if request.method == "POST":
        keyword = request.form["keyword"]
        result = "您輸入的關鍵字是：" + keyword

        Result = ""
        db = firestore.client()
        collection_ref = db.collection("圖書精選")
        docs = collection_ref.get()
        for doc in docs:
            bk = doc.to_dict()
            if keyword in bk["title"]:
                Result += "書名：<a href=" + bk["url"] + ">" + bk["title"] + "</a><br>"
                Result += "作者：" + bk["author"] + "<br>"
                Result += str(bk["anniversary"]) + "週年紀念版<br>"
                Result += "<img src=" + bk["cover"] + "> </img><br><br>"
        return Result
    else:
        return render_template("searchbooks.html")

@app.route("/spider")
def spider():
    url = "https://www1.pu.edu.tw/~tcyang/course.html"
    Data = requests.get(url)
    Data.encoding = "utf-8"
    sp = BeautifulSoup(Data.text, "html.parser")
    result=sp.select(".team-box")
    info = ""
    for x in result:
        info += "<a href=" + x.find("a").get("href") + ">" + x.text + "</a><br>"
        info += x.find("a").get("href") + "<br><br>"
    return info   
@app.route("/movie")
def movie():
  url = "http://www.atmovies.com.tw/movie/next/"
  Data = requests.get(url)
  Data.encoding = "utf-8"
  sp = BeautifulSoup(Data.text, "html.parser")
  result=sp.select(".filmListAllX li")
  lastUpdate = sp.find("div", class_="smaller09").text[5:]

  for item in result:
    picture = item.find("img").get("src").replace(" ", "")
    title = item.find("div", class_="filmtitle").text
    movie_id = item.find("div", class_="filmtitle").find("a").get("href").replace("/", "").replace("movie", "")
    hyperlink = "http://www.atmovies.com.tw" + item.find("div", class_="filmtitle").find("a").get("href")
    show = item.find("div", class_="runtime").text.replace("上映日期：", "")
    show = show.replace("片長：", "")
    show = show.replace("分", "")
    showDate = show[0:10]
    showLength = show[13:]

    doc = {
        "title": title,
        "picture": picture,
        "hyperlink": hyperlink,
        "showDate": showDate,
        "showLength": showLength,
        "lastUpdate": lastUpdate
      }

    db = firestore.client()
    doc_ref = db.collection("電影").document(movie_id)
    doc_ref.set(doc)    
  return "近期上映電影已爬蟲及存檔完畢，網站最近更新日期為：" + lastUpdate 
 

if __name__ == "__main__":
    app.run(debug=True)
    #serve(app, host='0.0.0.0', port=8080)