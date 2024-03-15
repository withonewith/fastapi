from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

class memoapp(BaseModel):
    text: str

memo_storage: Union[memoapp, None] = None
app = FastAPI()

# 메모 create
@app.post("/create/") 
async def create_item(memo: memoapp):
    # memo_storage 값 수정을 위해 전역 변수로 변경
    global memo_storage
    memo_storage = memo
    return memo_storage

# 메모 read
@app.get("/read/")
async def read_item():
    if memo_storage:
        return memo_storage
    return {"작성된 메모가 없습니다."}

# 메모 update
@app.put("/put/")
async def update_item(memo_update: memoapp):
    # memo_storage 값 수정을 위해 전역 변수로 변경
    global memo_storage
    if memo_storage:
        memo_storage = memo_update
        return memo_storage
    return {"작성된 메모가 없습니다."} 

# 메모 delete
@app.delete("/delete/")
async def delete_item():
    # memo_storage 값 수정을 위해 전역 변수로 변경
    global memo_storage
    if memo_storage:
        memo_storage = None
        return memo_storage
    return {"작성된 메모가 없습니다."} 