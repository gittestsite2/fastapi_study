"""
To receive uploaded files, first install python-multipart.
E.g. pip install python-multipart.
This is because uploaded files are sent as "form data".


1. Have in mind that this means that the whole contents will be stored in memory. This will work well for small files.
bytes / UploadFile
L 2개의 방식 차이 (상황에 따라서 어떠한 것을 사용하는가?)
L bytes : python의 기능
L uploadfile : StarletteUploadFile

bytes를 이용하면 파일을 메모리에 올리고 업로드 수행?
uploadfile을 이용하는것이 더욱 이점이 많다고 한다.
L 메모리 + Disk저장방식 혼합 사용

1. 의미 : special classes가 무슨 뜻일까?
File is a class that inherits directly from Form.
But remember that when you import Query, Path, File and others from fastapi,
those are actually functions that return special classes.

1. uploadfile 사용시 장점
  - It has a file-like async interface.
    L https://docs.python.org/3/glossary.html#term-file-like-object
  - SpooledTemporaryFile
    L https://docs.python.org/3/library/tempfile.html#tempfile.SpooledTemporaryFile


2. Union / Option / |
3. yield



"""

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()


# @app.post("/files/")
# async def create_file(file: bytes = File()):
#     # print(file)
#     return {"file_size": len(file)}
#
#
# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile):
#     return {"filename": file.filename}
#
#


# @app.post("/files/")
# async def create_file(file: bytes | None = File(default=None)):
#     if not file:
#         return {"message": "No file sent"}
#     else:
#         return {"file_size": len(file)}
#
#
# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile | None = None):
#     if not file:
#         return {"message": "No upload file sent"}
#     else:
#         return {"filename": file.filename}



# @app.post("/files/")
# async def create_file(file: bytes = File(description="A file read as bytes")):
#     return {"file_size": len(file)}
#
#
# @app.post("/uploadfile/")
# async def create_upload_file(
#     file: UploadFile = File(description="A file read as UploadFile"),
# ):
#     return {"filename": file.filename}



@app.post("/files/")
async def create_files(files: list[bytes] = File()):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

