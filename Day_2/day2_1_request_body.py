"""
Request Body
https://fastapi.tiangolo.com/ko/tutorial/body/

1. GET은 권장하지 않음
To send data, you should use one of: POST (the more common), PUT, DELETE or PATCH.


질문)
1. async def create_item(item: Item):
이 코드를 통해서 어떻게 Request Body에 대한 부분인 것을 인지 할수 있는가?
(*) Request Body부분에 대한 것이 명시적인 부분이 없어서 궁금
L body의 동일한 값을 이름으로 Query Param을 지정하니 정상동작 되었다.
L Postman

파이딕티

"""

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item, price: float = 0, name: str = "_blank"):
    # return item
    return {"name": item.name, "desc": item.description
        , "price(item)": item.price
            , "price(param)" : price
            , "name(param)" : name}



@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result