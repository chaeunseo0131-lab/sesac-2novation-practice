from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def ping():
    msg = {"msg" : "pong"}
    return msg
"""
- git push
git push 하는 source코드는 fastapi로 만든다.
fastapi로 get method의 api를 /ping 이라는 주소로 만들고,
{"msg": "OK"} 를 응답한다.

 uvicorn main:app
 
"""
@app.get("/ping")
def ping():
    msg = {"msg" : "OK"}
    return msg

