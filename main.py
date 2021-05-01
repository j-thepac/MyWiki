

# import redis
#
#
# r=redis.Redis('redis-19150.c252.ap-southeast-1-1.ec2.cloud.redislabs.com',19150,password='Fy3RFYIxMz34AHyeIkLGr8gYqlvpNgB5')
#
# r.set('foo', 'bar')
# value = r.get('foo')
# print(value)

from flask import Flask,render_template,json,jsonify,request

app=Flask(__name__)


@app.route("/",methods=["GET","POST"])
def fn():
    if(request.method=="GET"):return render_template("index.html")



if (__name__=="__main__"):app.run()


