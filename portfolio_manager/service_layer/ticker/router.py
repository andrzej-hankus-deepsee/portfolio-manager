from fastapi import APIRouter, Depends

from portfolio_manager.service_layer.ticker.schemas import TickerSchema
from portfolio_manager.shared.schemas import SuccessSchema
from portfolio_manager.bootstrap import get_bootstrap, Bootstrap

router = APIRouter()

@router.post("/",status_code=201)
async def create_ticker(
    ticker: TickerSchema, 
    bootstrap: Bootstrap = Depends(get_bootstrap),
) -> SuccessSchema:
    return {"success": await bootstrap.ticker_repository.create_one(ticker=ticker)}