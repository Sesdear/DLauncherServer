from fastapi import APIRouter, Path
from app.json_provider import get_json



router: APIRouter = APIRouter(
    prefix='/api/servers',
    tags=['servers']
)



@router.get("/{server}/data")
async def get_server_data(server: str = Path(..., description="Server name like 'server1'")) -> dict:
    json_data = get_json(f"servers/{server}")
    return json_data
