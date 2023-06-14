
import os
import time
from fastapi import FastAPI
from .exception import StoryException
from .router import blog_get
from .router import blog_post
from .router import user
from .router import article
from .router import product
from .router import file
from .router import dependencies
from .db import models
from .db.database import engine
from fastapi.responses import JSONResponse
from fastapi import Request
from .auth import authentication
from fastapi.staticfiles import StaticFiles
from .templates import templates
from .client import html
from starlette.responses import HTMLResponse
from fastapi.websockets import WebSocket
app = FastAPI(debug=True)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(authentication.router)
app.include_router(file.router)
app.include_router(templates.router)
app.include_router(dependencies.router)
@app.get("/hello")
def index():
    return {"message": "Hello World"}

@app.exception_handler(StoryException)
def story_exception_handler(request:Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={'detail': exc.name}
    )
# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#     return PlainTextResponse(str(exc), status_code = 400)
models.Base.metadata.create_all(engine)
current_directory = os.path.dirname(__file__)
files_path = os.path.join(current_directory, 'files')
template_path = os.path.join(current_directory, 'templates','static')
app.mount("/files", StaticFiles(directory=files_path),name='files')
app.mount("/templates/static", StaticFiles(
    directory=template_path
),name="static")

@app.middleware("http")
async def add_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    response.headers['duration'] = str(duration)
    return response

@app.get("/")
async def get():
    return HTMLResponse(html)
clients=[]
@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    while True:
        data = await websocket.receive_text()
        for client in clients:
            await client.send_text(data)