from fastapi import FastAPI

from app.routers import minecraft_repo_router, indexes_router, servers_router

app = FastAPI(title="DLauncherServer")

app.include_router(minecraft_repo_router)
app.include_router(indexes_router)
app.include_router(servers_router)

@app.get('/')
def root():
    return {"message": "DLauncherServer v1 Works"}