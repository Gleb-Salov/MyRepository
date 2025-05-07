from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    price: float = Field(..., gt=0)
    secret_code: str = Field(..., min_length=4)

fake_db = {}

 
@app.post(
    "/items/",
    response_model=Item,
    response_model_exclude={"secret_code"},
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"description": "Invalid input or item already exists"},
        201: {"description": "Item created successfully"},
    }
)
def create_item(item: Item):
    if item.name in fake_db:
        raise HTTPException(
            status_code=400,
            detail="Item already exists"
        )

    # сохраняем "в базу"
    fake_db[item.name] = item
    return item
