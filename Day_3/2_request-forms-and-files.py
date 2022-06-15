from fastapi import FastAPI, File, Form, UploadFile
app = FastAPI()


"""
install : pip install python-multipart

>>
1. form vs file
You can define files and form fields at the same time using File and Form.
"""


@app.post("/files/")
async def create_file(
    file: bytes = File(), fileb: UploadFile = File(), token: str = Form()
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
