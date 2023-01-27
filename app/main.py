from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def url():
    return {"mensaje":"Hello World"}

#hello mundo 