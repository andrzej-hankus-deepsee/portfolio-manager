from fastapi import APIRouter

from portfolio_manager.service_layer.portfolio.schemas import PortfolioSchema, PortfoliosSchema
from portfolio_manager.shared.schemas import SuccessSchema

router = APIRouter()


@router.post("/", status_code=201)
async def create_portfolio(portfolio: PortfolioSchema) -> SuccessSchema:
    return {"success": True}  # type: ignore


@router.get("/")
async def get_portfolios() -> PortfoliosSchema:
    return {
            "portfolios": [
                {
                    "id": 1,
                    "name": 'portfolio-1',
                    "cash": 100000.00,
                    "positions": [
                        {
                            'symbol': 'AAPL',
                            'shares': 100,
                            'price': 10.00,
                        },
                        {
                            'symbol': 'CMG',
                            'shares': 50,
                            'price': 5.00,
                        }
                    ]
                }
            ]
        }


@router.get("/{id}")
async def get_portfolio(id: int) -> PortfolioSchema:
    return {
                "id": 1,
                "name": 'portfolio-1',
                "cash": 100000.00,
                "positions": [
                        {
                            'symbol': 'AAPL',
                            'shares': 100,
                            'price': 10.00,
                        },
                        {
                            'symbol': 'CMG',
                            'shares': 50,
                            'price': 5.00,
                        }
                    ]
            }
