from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello_world():
    """Hello World"""
    return {"message": "hello, world"}


@app.get("/{name}")
async def hello_name(name: str):
    """Hello <name>"""
    return {"message": f"hello, {name}"}


@app.post("/addition")
async def addition(a: int, b: int):
    """Addition of two numbers"""
    result = a + b
    return {"result": result}


def main():
    """Main function."""
    pass


if __name__ == "__main__":
    main()
