from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
# async def login(username: str = Form(), password_tmp: str = Form()):
async def login(username: str, password_tmp: str ):
    print(username)
    print(password_tmp)
    return {"username": username, "password" : password_tmp}
