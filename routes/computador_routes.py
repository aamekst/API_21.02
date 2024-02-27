from fastapi import APIRouter


router = APIRouter()

@router.get('/api/v1/computador_router')
async def get_computadores():
    return {"info": "Todos os computadores"}