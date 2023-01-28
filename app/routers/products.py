from fastapi import APIRouter

router = APIRouter()

@router.get("/products")
async def products():
    return ["producto 1", "Producto 2", "Producto 3"]

