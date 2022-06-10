from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()


"""
1. 해당 Parameter가 Request body에서 정의된 항목을 명시함 : Body()
importance: int = Body()

2. Body(embed=True)
{ 
 "a" : "1"
}

{
  "item" : {
        "a" : "1"
  }
}
"""
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
#     q: str | None = None,
#     item: Item | None = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results




class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


# @app.put("/items_body/{item_id}")
# async def update_item(item_id: int, item: Item, user: User, importance: int = Body()):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     return results



# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int,
#     item: Item,
#     user: User,
#     importance: int = Body(gt=0),
#     q: str | None = None
# ):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     if q:
#         results.update({"q": q})
#     return results



@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
# async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
