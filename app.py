from fastapi import FastAPI
import uvicorn


from src import init_app
from src.config import load_config


if __name__ == "__main__":
    config = load_config()
    app = init_app(FastAPI())
    uvicorn.run(app, host=config.api.host, port=config.api.port)
