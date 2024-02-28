@echo off

REM Check if the Postgres image is already present
docker images | findstr "postgres"
IF ERRORLEVEL 1 (
    REM Pull the Postgres image
    docker pull postgres
)

REM Check if the Docker container is already running
docker ps -a | findstr "database-to-S203"
IF ERRORLEVEL 1 (
    REM Create and start the Docker container
    docker run --name database-to-S203 -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=root -d postgres
)

REM Attach a shell to the running container
docker start database-to-S203
docker exec -it database-to-S203 bash