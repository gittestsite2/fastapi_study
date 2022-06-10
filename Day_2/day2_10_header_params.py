from fastapi import FastAPI, Header

app = FastAPI()

"""
질문)
이것도 호출이? 어떤 방식인지
설정하는것인지, 정보를 호출하는 것인지??
"""

@app.get("/items/")
async def read_items(user_agent: str | None = Header(default=None)):
    return {"User-Agent": user_agent}
