#   Access application
    http://127.0.0.1:5000/anything (local)
    https://wikipedia-us.herokuapp.com/anything (heroku)

# Wiki  Project
    1. Display Wiki page
    2. It can be edited by Post request

    Note : 
    The DB used is Redis
    Post Request sets data into redis-server
    https://redis.io/


## Pre-Req:
    
    1. Install Python
    2. Install Virtualenv
    3. set REDIS_DEBUG, REDIS_URL , REDIS_PORT , REDIS_PASSWORD in your bashrc(linux) , bashprofile(mac)
    4. Restart system


## Steps:
    3. Activate Virtualenv
    4. pip install -r requirements.txt
    5. run main.py


## Application URL :
    http://127.0.0.1:5000/anything (local)


## Editing:
    
    POST:
        local-url  :http://127.0.0.1:5000
        
        Headers:
            Content-Type : application/json
    
        Body:
            {
              "body": "This article is about the writing implement. For other uses, see",
              "title": "football"
            }


## Procfile example:

            from flask import Flask
            my_awesome_app = Flask(__name__)
            
            
            @my_awesome_app.route('/')
            def hello_world():
                return 'Hello World!'
            
            
            if __name__ == '__main__':
                my_awesome_app.run()

    Then you will add the following line in your Procfile
    web: gunicorn run:my_awesome_app