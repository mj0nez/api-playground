from __future__ import annotations

import structlog
from litestar import Litestar
from litestar.logging import StructLoggingConfig
from litestar.middleware.logging import LoggingMiddlewareConfig

from playground.litestar_app.routes import (
    InteractionsController,
    get_sample,
    get_user,
)

logger = structlog.get_logger(__name__)


logging_config = StructLoggingConfig()
logging_middleware_config = LoggingMiddlewareConfig()

app = Litestar(
    route_handlers=[
        get_sample,
        get_user,
        InteractionsController,
    ],
    logging_config=logging_config,
    debug=True,
    # middleware=[logging_middleware_config.middleware],
)
