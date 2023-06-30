from fastapi import APIRouter, Depends, HTTPException

from portfolio_manager.bootstrap import get_bootstrap, Bootstrap
from portfolio_manager.service_layer.portfolio.schemas import PortfolioSchema, PortfoliosSchema, OrderSchema, CreatePortfolioSchema
from portfolio_manager.shared.schemas import SuccessSchema
from portfolio_manager.domain.models import PositionOrder


router = APIRouter()


@router.post("/", status_code=201)
async def create_portfolio(
        portfolio: CreatePortfolioSchema,
        bootstrap: Bootstrap = Depends(get_bootstrap),
) -> SuccessSchema:
    return {"success": await bootstrap.portfolio_repository.create_one(portfolio=portfolio)}


@router.get("/")
async def get_portfolios(
        bootstrap: Bootstrap = Depends(get_bootstrap),
) -> PortfoliosSchema:
    return {"portfolios": await bootstrap.portfolio_repository.get_many()}


@router.get("/{id}")
async def get_portfolio(
        id: int,
        bootstrap: Bootstrap = Depends(get_bootstrap)
) -> PortfolioSchema:
    portfolio = await bootstrap.portfolio_repository.get_one(id_=id)
    
    if portfolio is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    
    return portfolio

@router.post("/order/",status_code=201)
async def create_order(
    order_data: OrderSchema,
    bootstrap: Bootstrap = Depends(get_bootstrap),
) -> SuccessSchema:
    ticker = await bootstrap.ticker_repository.get_one(order_data.position_order.ticker.symbol)

    if ticker is None:
        raise HTTPException(status_code=404, detail="Ticker not found")

    position_order = PositionOrder(
        ticker=ticker,
        shares=order_data.position_order.shares,
        max_price=order_data.position_order.max_price
        )
    
    result = await bootstrap.portfolio_repository.add_postion_order(
            portfolio_id=order_data.portfolio_id,
            position_order=position_order
        )
    if not result:
        raise HTTPException(status_code=400, detail="Order not created")
    return {"success": result}