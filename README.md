
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