from fastapi import FastAPI, Query
from typing import Union

"""

query param에 필수값 체크, Validation체크 기능

1. 필수 (타입만 정의하고 별다른 옵션을 기록하지 않는다)
async def read_items(q: str)
2. Validation 
Query을 이용해서 적용


str | None | int : parameter에 허용되는 타입 정의
= : default값을 정의 (None, "AAA", 111등등 default값 정의)
Query(default=None, max_length=50) : 조건을 넣기

2. 2개는 같은 역활을 한다.
* Query를 통해서 조금더 다양한 Validation 구성을 지원한다.
(q: str | None = Query(default="AAA")):
(q: str | None = "AAA"):

* None를 사용하면 필수 required가 아님
as it will use that None as the default value, and that way make the parameter not required.


3. 필수값 정의하기
* default값을 정의하지 않으면, 필수 required로 식별한다.
* async def read_items(q: str = Query(default=Required, min_length=3)):
  L 명시적으로 정의하는 방식
* async def read_items(q: str | None = Query(default=..., min_length=3)):
  L Ellipsis를 사용하는 방식


4. Required with Ellipsis (...)
* ...을 사용하면, 필수값 체크가 된다.
* https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#required-with-ellipsis
* https://tech.madup.com/python-ellipsis/


질문)
1. title 부분은 swagger부분에 어디서 표시가 되는것일까요?  
q: str | None = Query(default=None, title="Query string", min_length=3)
https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#declare-more-metadata

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