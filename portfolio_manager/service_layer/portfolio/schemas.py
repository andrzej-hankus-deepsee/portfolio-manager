from portfolio_manager.shared.schemas import BaseSchema
from portfolio_manager.service_layer.ticker.schemas import TickerSchema
class PositionSchema(BaseSchema):
    ticker: TickerSchema
    shares: int
    buying_price: float

class PositionOrderSchema(BaseSchema):
    ticker: TickerSchema
    shares: int
    max_price: float

class PortfolioSchema(BaseSchema):
    id : int | None = None
    name: str
    cash: float
    positions: list[PositionSchema]
    orders: list[PositionOrderSchema]

class PortfoliosSchema(BaseSchema):
    portfolios: list[PortfolioSchema]