from fastapi import FastAPI
from pydantic import BaseModel


class Calculator(BaseModel):
    firstnum: int
    secondnum: int


app = FastAPI()


@app.post("/calculator/")
async def create_item(num: Calculator):
    result = num.firstnum + num.secondnum
    return {f'Calculation result is {result}.'}