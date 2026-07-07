from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class TelemetryUser(BaseModel):
    uuid: UUID
    timestamp: datetime = Field(default_factory=datetime.now)
    system: str

class TelemetryStatsResponse(BaseModel):
    total_users: int
    today_users: int
    systems_percentage: dict[str, float]