import firebase_admin
from firebase_admin import credentials,firestore


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
docs = [
{
      "title": "無聲夜",
      "picture": "http://www.atmovies.com.tw/photo101/fsus15799866/pl_fsus15799866_0005.jpg",
      "hyperlink": "http://www.atmovies.com.tw//movie/fsus15799866/",
      "showDate": "2023/12/01",
      "showLength": "120",
      "lastUpdate": "2023/11/25"
  },
  {
      "title": "旺卡",
      "picture": "http://www.atmovies.com.tw/photo101/fwen26166392/pl_fwen26166392_0018.jpg",
      "hyperlink": "http://www.atmovies.com.tw//movie/fwen26166392/",
      "showDate": "2023/12/06",
      "showLength":" " ,
      "lastUpdate":"2023/11/25"
  },
  {
      "title": "人犬",
      "picture": " http://www.atmovies.com.tw/photo101/fden17009348/pl_fden17009348_0002.jpg",
      "hyperlink": " http://www.atmovies.com.tw//movie/fden17009348/",
      "showDate": "2023/12/15",
      "showLength": "113",
      "lastUpdate": "2023/11/25"
  },
  {
      "title": "水行俠 失落王國",
      "picture": " http://www.atmovies.com.tw/photo101/faen39663764/pl_faen39663764_0002.jpg",
      "hyperlink": " http://www.atmovies.com.tw//movie/faen39663764/",
      "showDate": "2023/12/20",
      "showLength": " " ,
      "lastUpdate": "2023/11/25"
  },
  {
      "title": "星願",
      "picture": "http://www.atmovies.com.tw/photo101/fwen11304740/pl_fwen11304740_0002.jpg",
      "hyperlink": " http://www.atmovies.com.tw//movie/fwen11304740/",
      "showDate": "2023/12/29",
      "showLength": " " ,
      "lastUpdate": "2023/11/25"
  },
  {
      "title": "金手指",
      "picture": " http://www.atmovies.com.tw/photo101/fgth14099796/pl_fgth14099796_0001.jpg",
      "hyperlink": " http://www.atmovies.com.tw//movie/fgth14099796/",
      "showDate": "2023/12/30",
      "showLength": " " ,
      "lastUpdate": "2023/11/25"
  },
  {
      "title": "機密特務: 阿蓋爾",
      "picture": "http://www.atmovies.com.tw/photo101/faen15009428/pl_faen15009428_0002.jpg",
      "hyperlink": "http://www.atmovies.com.tw//movie/faen15009428/",
      "showDate": "2024/02/02",
      "showLength": " " ,
      "lastUpdate": "2023/11/25"
  },
  {
      "title": "飛鴨向前衝",
      "picture": "http://www.atmovies.com.tw/photo101/fmen56495056/pl_fmen56495056_0008.jpg",
      "hyperlink": "http://www.atmovies.com.tw//movie/fmen56495056/",
      "showDate": "2024/02/08",
      "showLength": " " ,
      "lastUpdate": "2023/11/25"
  },
  {
      "title": "蜘蛛夫人",
      "picture": "http://www.atmovies.com.tw/photo101/fmen11057302/pl_fmen11057302_0001.jpg",
      "hyperlink": "http://www.atmovies.com.tw//movie/fmen11057302/",
      "showDate": "2024/02/14",
      "showLength": " " ,
      "lastUpdate": "2023/11/25"
  },
  {
      "title": "艾立歐：第三星公關",
      "picture": " http://www.atmovies.com.tw/photo101/feen84900148/pl_feen84900148_0003.jpg",
      "hyperlink": "http://www.atmovies.com.tw//movie/feen84900148/",
      "showDate": "2024/03/01",
      "showLength": " " ,
      "lastUpdate": "2023/11/25"
  },
  {
      "title": "GHOSTBUSTERS：冰天凍地",
      "picture": " http://www.atmovies.com.tw/photo101/fgen21235248/pl_fgen21235248_0001.jpg",
      "hyperlink": " http://www.atmovies.com.tw//movie/fgen21235248/",
      "showDate": "2024/04/03",
      "showLength": " " ,
      "lastUpdate": "2023/11/25"
  },
  {
      "title": "功夫熊貓 4",
      "picture": " http://www.atmovies.com.tw/photo101/fken21692408/pl_fken21692408_0001.jpg",
      "hyperlink": "http://www.atmovies.com.tw//movie/fken21692408/",
      "showDate": "2024/04/05",
      "showLength": " " ,
      "lastUpdate": "2023/11/25"
  },
  {
      "title": "挑戰者",
      "picture": " http://www.atmovies.com.tw/photo101/fcen16426418/pl_fcen16426418_0001.jpg",
      "hyperlink": "http://www.atmovies.com.tw//movie/fcen16426418/",
      "showDate": "2024/04/26",
      "showLength": " " ,
      "lastUpdate": "2023/11/25"
  },
  {
      "title": "特技玩家",
      "picture": "http://www.atmovies.com.tw/photo101/ffen41684562/pl_ffen41684562_0002.jpg",
      "hyperlink":"http://www.atmovies.com.tw//movie/ffen41684562/",
      "showDate": "2024/05/01",
      "showLength": " " ,
      "lastUpdate": "2023/11/25"
  },
  {
      "title": "猩球崛起：王國誕生",
      "picture": "http://www.atmovies.com.tw/photo101/fken11389872/pl_fken11389872_0001.jpg",
      "hyperlink": "http://www.atmovies.com.tw//movie/fken11389872/",
      "showDate": "2024/05/24",
      "showLength": " " ,
      "lastUpdate": "2023/11/25"
  },
  {
      "title": "腦筋急轉彎2",
      "picture": " http://www.atmovies.com.tw/photo101/fien22022452/pl_fien22022452_0001.jpg",
      "hyperlink": "http://www.atmovies.com.tw//movie/fien22022452/",
      "showDate": "2024/06/14",
      "showLength": " " ,
      "lastUpdate": "2023/11/25"
  },
  {
      "title": "獵人克萊文",
      "picture": "http://www.atmovies.com.tw/photo101/fken58790086/pl_fken58790086_0001.jpg",
      "hyperlink": "http://www.atmovies.com.tw//movie/fken58790086/",
      "showDate": "2024/08/28",
      "showLength": " " ,
      "lastUpdate": "2023/11/25"
  }      
  ]

db = firestore.client()
collection_ref = db.collection("電影")
for doc in docs:
      collection_ref.add(doc)