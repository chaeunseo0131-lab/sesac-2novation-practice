# fastAPI로 get method의 api를 ping이라는 주소로 만들고, {"msg":"OK"}를 응답하기.
from fastapi import FastAPI

app = FastAPI() # FastAPI 클래스 객체할당

@app.get("/")   # app객체의 메소드 get(조회Read)도 있고 post(생성), put(수정Update), delete 등..
def ping():
    msg={"msg" : "pong"}
    return msg

@app.get("/ping")
def ok():
    msg={"msg":"OK"}
    return msg

"""
API     : 클라이언트가 요청할 수 있는 하나의 기능(주소 + 요청방식(메서드 get post..)
FastAPI : 웹 앱으로 API를 만들 수 있게 해줌
uvicorn : 웹 서버로 requset response를 FastAPI에 전달 (API를 실행시켜주는 서버프로그램임)

웹서버 실행 시킬 때 : uvicorn main:app 
uvicorn -> 서버야
main    -> main.py 파일
app     -> py 파일 안에 있는 FastAPI 인스턴스 이름. app객체 실행시켜라

실행시 나오는 주소 : http://127.0.0.1:8000
http://127.0.0.1   -> localhost 내pc
:8000              -> 포트 번호 (컴터 내 돌고 있는 서비스 번호)

웹서버주소/docs : API목록과 정보 볼 수 있음

서버 종료 : ctrl + c
"""