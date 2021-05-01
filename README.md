
# Wiki  Project
    1. Display Wiki page
    2. It can be edited by Post request


    Note : 
    The DB used is Redis
    Post Request sets data into redis-server
    https://redis.io/



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