from fastapi import APIRouter
from app.json_provider import get_json



router: APIRouter = APIRouter(
    prefix='/api/index',
    tags=['indexes']
)

@router.get('')
@router.get('/')
async def get_minecraft_repos() -> dict:
    _json_data = get_json("index")
    return _json_data
