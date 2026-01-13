from fastapi import APIRouter
from app.json_provider import get_json



router: APIRouter = APIRouter(
    prefix='/api/minecraft_repos',
    tags=['minecraft-repos']
)

@router.get('')
@router.get('/')
async def get_minecraft_repos() -> dict:
    _json_data = get_json("minecraft_repo")
    return _json_data