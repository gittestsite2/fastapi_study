from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: list = []
    # tags: List[str] = []
    # tags: list[str] = []
    # tags: set[str] = set()

    # "tags": [
    #   1,
    #   2,
    #   3,
    #   4,
    #   5
    # ]

    # "tags": [
    #   "2",
    #   "1",
    #   "24445",
    #   "3"
    # ]


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results