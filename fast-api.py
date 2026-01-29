import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/secrets")
def signs():
    data = {"industry": "coding", "weatlh": "generational"}
    return data


@app.get("/")
def home():
    data = {"name": "enos", "weatlh": "millionaire"}
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8100)
