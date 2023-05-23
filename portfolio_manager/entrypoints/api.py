from fastapi import FastAPI

from portfolio_manager.service_layer.portfolio.router import router as portfolios_router
from portfolio_manager.service_layer.ticker.router import router as tickers_router

API_PREFIX = "/api/v1"

api = FastAPI(
    title="Portfolio Manager API",
    version="1.0.0",
    docs_url="/api/v1/docs",
    redoc_url=None,
)

api.include_router(tickers_router, prefix=f"{API_PREFIX}/tickers", tags=["tickers"])
api.include_router(portfolios_router, prefix=f"{API_PREFIX}/portfolios", tags=["portfolios"])
