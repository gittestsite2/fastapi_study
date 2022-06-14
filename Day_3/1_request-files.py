"""
To receive uploaded files, first install python-multipart.
E.g. pip install python-multipart.
This is because uploaded files are sent as "form data".


1. Have in mind that this means that the whole contents will be stored in memory. This will work well for small files.
bytes / UploadFile
L 2개의 방식 차이 (상황에 따라서 어떠한 것을 사용하는가?)

2. Union / Option / |
3. yield



"""

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}