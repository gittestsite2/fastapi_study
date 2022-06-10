from typing import Union

from fastapi import FastAPI, Path, Query

app = FastAPI()

"""

질문)
1. Path명명과 title관련
https://fastapi.tiangolo.com/ko/tutorial/path-params-numeric-validations/#_3
* item_id: int = Path(title="The ID of the item to get"),
* item_id: int ,
위 2개의 사항의 차이는 무엇인가?

2. *, 매개변수 정렬관련
https://fastapi.tiangolo.com/ko/tutorial/path-params-numeric-validations/#_5
* 정확히 어떠한 역활, 의미 파악 필요



"""

# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: int = Path(title="The ID of the item to get"),
#     q: Union[str, None] = Query(default=None, alias="item-query"),
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q2": q})
#     return results



# @app.get("/items/{item_id}")
# async def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q3": q})
#     return results


@app.get("/items/{item_id}")
async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results