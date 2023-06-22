from portfolio_manager.shared.schemas import BaseSchema

class PositionSchema(BaseSchema):
    symbol: str
    shares: int
    price: float

class PortfolioSchema(BaseSchema):
    id : int | None = None
    name: str
    cash: float
    positions: list[PositionSchema]

class PortfoliosSchema(BaseSchema):
    portfolios: list[PortfolioSchema]