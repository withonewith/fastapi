from fastapi import FastAPI

app = FastAPI()


@app.get("/{username}")
async def read_item(username):
    return {f"Hello, {username}!"}