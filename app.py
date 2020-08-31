import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

tags = [{
    "name": "test",
    "description": "test endpoint",
    "externalDocs": {
        "description": "url bearing",
        "url": "https://bearing.ai"
    }
}]
app = FastAPI(title='API', description='description', openapi_tags=tags)


class Test(BaseModel):
    name: str
    description: str
    number: int


@app.get("/", tags=['test'])
async def root():
    return {"message": "Hello World"}


@app.get("/{value}&{value2}", tags=['test'])
async def get_value(value: int, value2: int):
    print(value)
    return {"message": value2}


@app.post("/test", tags=['test'])
async def test(test: Test):
    print(test)
    return test


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=5000, debug=True)
