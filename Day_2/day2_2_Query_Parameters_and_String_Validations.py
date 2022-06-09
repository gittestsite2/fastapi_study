from fastapi import FastAPI, Query
from typing import Union

"""
query param에 필수값 체크, Validation체크 기능

1. 필수 (타입만 정의하고 별다른 옵션을 기록하지 않는다)
async def read_items(q: str)
2. Validation 
Query을 이용해서 적용

"""
app = FastAPI()

@app.get("/items/")
# async def read_items(q: str | None = Query(default=None, max_length=50)):
# async def read_item(skip: int = 0, limit: int = 10):
# async def read_items(item_id: str, q: Union[str, None] = None)
# # async def read_items(q: str | None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    # user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
    user_id: int, item_id: str = None, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item