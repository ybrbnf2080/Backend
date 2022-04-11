import uvicorn
from . settings import settings

uvicorn.run(
    "WeGo.app:app",
    reload=True,
    host=settings.server_host,
    port=settings.server_port,
    log_level="info"
)
