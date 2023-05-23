from fastapi import APIRouter, Depends

from portfolio_manager.service_layer.ticker.schemas import TickerSchema
from portfolio_manager.shared.schemas import SuccessSchema

router = APIRouter()


@router.post("/",status_code=201)
async def create_ticker(ticker: TickerSchema) -> SuccessSchema:
    return {"success": True}  # type: ignore
