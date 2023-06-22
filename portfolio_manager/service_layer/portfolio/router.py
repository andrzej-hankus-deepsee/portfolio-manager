from fastapi import APIRouter, Depends, HTTPException

from portfolio_manager.bootstrap import get_bootstrap, Bootstrap
from portfolio_manager.service_layer.portfolio.schemas import PortfolioSchema, PortfoliosSchema
from portfolio_manager.shared.schemas import SuccessSchema

router = APIRouter()


@router.post("/", status_code=201)
async def create_portfolio(
        portfolio: PortfolioSchema,
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
        raise HTTPException(status_code=404, detail="Item not found")
    
    return portfolio
