from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ProductSchema(BaseModel):

    id: int
    nombre: str
    precio: float


# BASE DE DATOS EN MEMORIA
products = []


# GET ALL
@router.get("/products")
async def get_products():

    return products


# CREATE
@router.post("/products")
async def create_product(
    data: ProductSchema
):

    new_item = data.dict()

    products.append(new_item)

    return {
        "message": "Product creado",
        "data": new_item
    }


# UPDATE
@router.put("/products/{id}")
async def update_product(
    id: int,
    data: ProductSchema
):

    updated_item = data.dict()

    for index, item in enumerate(products):

        if item.get("id") == id:

            products[index] = updated_item

            return {
                "message": "Product actualizado",
                "data": updated_item
            }

    return {
        "error": "Product no encontrado"
    }


# DELETE
@router.delete("/products/{id}")
async def delete_product(id: int):

    for index, item in enumerate(products):

        if item.get("id") == id:

            deleted = products.pop(index)

            return {
                "message": "Product eliminado",
                "data": deleted
            }

    return {
        "error": "Product no encontrado"
    }
