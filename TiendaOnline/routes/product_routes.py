from fastapi import APIRouter

router = APIRouter()

# GET ALL
@router.get("/products")
async def get_products():

    return {"message": "Lista de Product"}


# CREATE
@router.post("/products")
async def create_product():

    return {"message": "Product creado"}


# UPDATE
@router.put("/products/{id}")
async def update_product(id: int):

    return {"message": "Product actualizado"}


# DELETE
@router.delete("/products/{id}")
async def delete_product(id: int):

    return {"message": "Product eliminado"}
