"""
Request Body
https://fastapi.tiangolo.com/ko/tutorial/body/

1. GET은 권장하지 않음
To send data, you should use one of: POST (the more common), PUT, DELETE or PATCH.

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
async def create_item(item: Item):
    return item
