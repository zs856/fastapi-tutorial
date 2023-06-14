import os
from fastapi import APIRouter, BackgroundTasks, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from ..custom_log import log
from ..schemas import ProductBase
router = APIRouter(
    prefix='/tempates',
    tags=['templates']
)
current_directory = os.path.dirname(__file__)
templates = Jinja2Templates(directory=current_directory)
@router.post("/products/{id}",response_class=HTMLResponse)
def get_product(id: str, product: ProductBase, request: Request, bt: BackgroundTasks):
    bt.add_task(log_template_call, f"Template read for product with id {id}")
    #product_template_path = os.path.join(current_directory,"product.html")
    return templates.TemplateResponse(
        "product.html",
        {
            "request": request,
            "id":id,
            "title":product.title,
            "description": product.description,
            "price": product.price
        }
    )

def log_template_call(message:str):
    log("MyAPI", message)