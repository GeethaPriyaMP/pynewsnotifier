import requests,json

def getustrendingnews():
    params = {
        'country':'us',
        'apiKey':'2819871d216e4b249c2a3bf39147ee16'
    }
    res = requests.get('https://newsapi.org/v2/top-headlines',params)
    jsonText =json.loads(res.text)
    articles = jsonText["articles"] 
    count = 0
    for item in articles:
        count = count + 1
        if count > 5:
            break
        print("US News:")
        print("News" ,count, ":" ,item["title"])


def getintrendingnews():
    params = {
        'country':'in',
        'apiKey':'2819871d216e4b249c2a3bf39147ee16'
    }
    res = requests.get('https://newsapi.org/v2/top-headlines',params)
    jsonText =json.loads(res.text)
    articles = jsonText["articles"] 
    count = 0
    for item in articles:
        count = count + 1
        if count > 5:
            break
        print("INDIA News:")
        print("News" ,count, ":" ,item["title"])
    
getustrendingnews()
getintrendingnews()
 
 
 
 