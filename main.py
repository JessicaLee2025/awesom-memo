from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

class Memo(BaseModel):
  id:str
  content:str
  
memos = []

@app.post("/memos")
def create_memo(memo:Memo):
    memos.append(memo)
    return {"message": "메모 추가에 성공했음!"}
  
@app.get("/memos")  
def read_memo():
  return memos
  
@app.put("/memos/{id}")
def put_memo(req_memo:Memo):
  for memo in memos:
    if memo.id== req_memo.id:
      memo.content=req_memo.content
      return "성공"
  return "그런건 없습니다!"

@app.delete("/memos/{memo_id}")
def delete_memo(memo_id:str):
  for index,memo in enumerate(memos):
    if memo.id== memo.id:
       memos.pop(index)
       return "성공"
  return "그런건 없습니다!"

app.mount("/", StaticFiles(directory="static", html=True),name="static")
