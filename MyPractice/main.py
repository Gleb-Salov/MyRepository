# uvicorn main:app --reload
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/hello")
def hello():
    return {"message": "Привет от FastAPI"}

from fastapi import FastAPI, Path, Query, HTTPException

app = FastAPI()

from fastapi import FastAPI, Path, Query, HTTPException

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(
    item_id: int = Path(..., title="ID товара"),  # ID должен быть больше 0
    name: str = Query(None, min_length=2, max_length=50)
):
    # Если item_id меньше 0, возбуждаем исключение
    if item_id <= 0:
        raise HTTPException(status_code=400, detail="ID должен быть больше или равен 1")
    
    return {
        "item_id": item_id,
        "filter_name": name
    }

@app.get("/products/{product_id}")
def get_product(
    product_id: int = Path(..., ge=10, le= 1000),
    category: str = Query(None, min_length=3, max_length=15)
):
    return{
        "product_id": product_id,
        "category": category
    }

class Product(BaseModel):
    name: str = Field(..., min_length=2, max_length=30)
    price: float = Field(..., gt=0, description="Цена товара должна быть > 0")
    in_stock: Optional[bool] = True

@app.post("/products/")
def create_product(product: Product):
    return{
        "message": "Product created succesfully",
        "product": product
    }