from fastapi import APIRouter
from app.json_provider import get_json



router: APIRouter = APIRouter(
    prefix='/api/servers',
    tags=['servers']
)


@router.get('/server1/data')
async def get_minecraft_repos() -> dict:
    _json_data = get_json("servers/server1")
    return _json_data
