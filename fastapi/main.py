from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Addition(BaseModel):
    a: int
    b: int


@app.get("/")
async def hello_world():
    """Hello World"""
    return {"message": "hello, world"}


@app.get("/{name}")
async def hello_name(name: str):
    """Hello <name>"""
    return {"message": f"hello, {name}"}


@app.post("/addition")
async def addition(payload: Addition):
    """Addition of two numbers"""
    result = payload.a + payload.b
    return {"result": result}


def main():
    """Main function."""
    pass


if __name__ == "__main__":
    main()
