

from flask import Flask,render_template,json,jsonify,request
import redis
import os
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
app=Flask(__name__)
debug=os.environ.get("REDIS_DEBUG")
url = os.environ.get("REDIS_URL")
port = os.environ.get("REDIS_PORT")
password = os.environ.get("REDIS_PASSWORD")
r = redis.Redis(url, port, password=password)


class RedisObject:
    def __init__(self,title,body):
        self.title=title
        self.body=body

def redis_set(redisobject:RedisObject):
    try:

        r.set('title', redisobject.title)
        r.set('body', redisobject.body)
    except Exception as ex:
        print("Redis server not operational")
        print(str(ex))


def redis_get():
    try:
        title=r.get('title').decode('utf-8')
        body=r.get('body').decode('utf-8')
        return RedisObject(title,body)
    except Exception as ex:
        print("Redis server not operational")
        print(str(ex))

@app.route("/<string:resource>",methods=["GET"])
def fn_get(resource):
    try:
        if(request.method=="GET"):
            return render_template("index.html",data=redis_get())
        else:
            return "not Implemented"
    except Exception as ex:
        print(str(ex))
        return "Fail"


@app.route("/",methods=["POST"])
def fn_post():
    try:
        if (request.method == "POST"):
            if(request.headers["content-type"]=="application/json"):
                data=(request.json)
                title=data["title"]
                body=data["body"]
                redis_set(RedisObject(title,body))
                return ("Pass:"+str(json.dumps(data)))
        else:
            return "not Implemented"
    except Exception as ex:
        print(str(ex))
        return "Fail"


 #app.run(host='0.0.0.0', port="5432",debug=True)
if (__name__=="__main__"):app.run(host="localhost",debug=debug)
    
