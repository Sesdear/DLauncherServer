from fastapi import APIRouter, status, Response, Depends
from app.json_provider import get_json
from app.models import TelemetryUser, TelemetryStatsResponse
from app.database import Database

database = Database()


router: APIRouter = APIRouter(
    prefix='/api/telemetry',
    tags=['telemetry']
)

@router.post('', status_code=status.HTTP_204_NO_CONTENT)
@router.post('/', status_code=status.HTTP_204_NO_CONTENT)
def save_telemetry(user_data: TelemetryUser, conn = Depends(database.get_db)):
    database.insert_user(conn, user_data)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get('/stats', response_model=TelemetryStatsResponse)
def get_stats(conn = Depends(database.get_db)):
    stats = database.get_telemetry_stats(conn)
    return stats