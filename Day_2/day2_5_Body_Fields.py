from fastapi import Body, FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()

"""

질문)
1. 여러가지 모델? 이 있다.
Query
Body
Path
Field

* 종류가 많이 있다
Path()
Query()
Header()
Cookie()
Body()
Form()
File()
https://fastapi.tiangolo.com/ko/tutorial/schema-extra-example/#example-and-examples-in-openapi


Query에서도 max_length체크하는 부분이 있고, 어떤때 어떤 기능을 사용해야 하는것이 정해진것인가?
아래 Field부분에 Query를 사용해도 되는가? 

https://fastapi.tiangolo.com/ko/tutorial/body-fields/#declare-model-attributes

description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")

> Body, Path, Query로 변경해서 테스트 해보면 정상적으로 동작을 한다. ??
  사용하는 기준이 있는가?
> Field works the same way as Query, Path and Body, it has all the same parameters, etc.

밑에 Technical Details, Tip이 존재한다.

"""
class Item(BaseModel):
    name: str
    description: str | None = Query(
        default=None, title="The description of the item", max_length=4
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
