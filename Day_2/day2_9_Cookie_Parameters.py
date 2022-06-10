from fastapi import Cookie, FastAPI

app = FastAPI()

"""
질문)
1. Cookie를 생성하는것? 해당 역활이 궁금

curl -X 'GET' \
  'http://127.0.0.1:8000/items/' \
  -H 'accept: application/json' \
  -H 'Cookie: ads_id=121'

2. 해당 API를 사용하려먼, 
   http://127.0.0.1:8000/items/?ads_id=aaa
   아래와 같이 호출하며 될까? 
"""
@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}
