# DLauncherServer
Special API Server on FastAPI for DLauncher4 1.5.0.0 or above
## RU
Этот api сервер сделан специально для DLauncher4 1.5.0.0 и выше для облегчения разработки и привидения всего к одному стандарту манифестов \
Система скачивания сборок переделана под контроль версий гит для более удобных обновлений 

В папке `ServerArchitecture` находиться документация по файлам проекта и по тому как устроенна система манифестов




### Api returns

`/api/index` GET return json from `app/jsons/index.json` \
`/api/minecraft_repos` GET return json from `app/jsons/minecraft_repo.json` \
`/api/servers/exampleServer1/data` GET return json from `app/jsons/servers/exampleServer.json`

Для добовления нового сервера просто закинуть `<server name>.json` в app/jsons/servers/


### Развертывание
Клонировать репозиторий
`git clone https://github.com/Sesdear/DLauncherServer.git`

#### Self start
`uvicorn app.main:app --reload`

#### Docker
Docker bind to port 6060, to change edir docker-compose.yaml
`docker-compose up -d` / `docker compose up -d`
