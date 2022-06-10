import base64

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/dynamic_params/")
async def dynamic_params(item: Item, qry: str | None = None):

    """
    qry_text : q=a&q2=b&q3=c&q4=d&q5=f

    qrys_decode_text=cT1hJnEyPWImcTM9YyZxND1kJnE1PWY=
    qry_encode_text=>q=a&q2=b&q3=c&q4=d&q5=f
    """
    # encoding
    # qry_bytes = qry.encode('ascii')
    # qry_base64 = base64.b64encode(qry_bytes)
    # qry_decode_text = qry_base64.decode('ascii')

    # decoding
    base64_bytes = qry.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    qry_encode_text = message_bytes.decode('ascii')

    item_dict = item.dict()

    if qry:
        arr_qry = qry_encode_text.split("&")

        for data in arr_qry:
            key_value = data.split("=")

            qry_key = key_value[0]
            qry_value = key_value[1]
            item_dict.update({qry_key: qry_value})

    return item_dict