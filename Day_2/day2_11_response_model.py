from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

"""


질문)
1. 결과값은 동일한데, response_model의 의미를 정확한 의미를 다시 파악 필요합니다.
@app.post("/items/", response_model=Item)
@app.post("/items/")

참고 링크
https://velog.io/@kjh03160/Fast-API-Response-Model-Output-%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%98%95%EC%8B%9D

"""
# @app.post("/items/", response_model=Item)
@app.post("/items/")
async def create_item(item: Item):
    return item



# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: str | None = None


# Don't do this in production!
# @app.post("/user/", response_model=UserIn)
# async def create_user(user: UserIn):
#     return user