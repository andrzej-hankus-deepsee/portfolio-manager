from fastapi import APIRouter, Depends

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
    return {"portfolios": []}


@router.get("/{id}")
async def get_portfolio(
        id_: int,
        bootstrap: Bootstrap = Depends(get_bootstrap)
) -> PortfolioSchema:
    return {}
