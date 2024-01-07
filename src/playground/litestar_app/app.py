from __future__ import annotations

from pathlib import Path

import structlog
import uvicorn
from litestar import Litestar
from litestar.logging import StructLoggingConfig
from litestar.middleware.logging import LoggingMiddlewareConfig

from playground.litestar_app.routes import (
    get_sample,
    get_user,
    post_interaction_msgspec,
    post_interaction_pydantic,
)

logger = structlog.get_logger(__name__)


logging_config = StructLoggingConfig()
logging_middleware_config = LoggingMiddlewareConfig()

app = Litestar(
    route_handlers=[
        get_sample,
        get_user,
        post_interaction_msgspec,
        post_interaction_pydantic,
    ],
    logging_config=logging_config,
    # middleware=[logging_middleware_config.middleware],
)
app_entrypoint = f"{Path(__file__).stem}:app"

if __name__ == "__main__":
    uvicorn.run(
        app_entrypoint,
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        # reload=True,
    )
