from fastapi import FastAPI

from app.routers import minecraft_repo_router, indexes_router, servers_router, telemetry_router
from app.database import Database

VERSION="1.1"




database = Database()
database.init_db()

app = FastAPI(title="DLauncherServer")

app.include_router(minecraft_repo_router)
app.include_router(indexes_router)
app.include_router(servers_router)
app.include_router(telemetry_router)

@app.get('/')
def root():
    return {"message": f"DLauncherAPI v{VERSION}"}

    