import uvicorn

from config.server_config import get_server_config

if __name__ == "__main__":
    server_config = get_server_config()

    uvicorn.run(
        app="server.server_api:app",
        host=server_config.host,
        port=server_config.port,
        reload=server_config.reload
    )

