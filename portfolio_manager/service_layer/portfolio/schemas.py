from portfolio_manager.shared.schemas import BaseSchema
from portfolio_manager.service_layer.ticker.schemas import TickerSchema
from portfolio_manager.bootstrap import get_bootstrap, Bootstrap
class PositionSchema(BaseSchema):
    ticker: TickerSchema
    shares: int

class PortfolioSchema(BaseSchema):
    id : int | None = None
    name: str
    cash: float
    positions: list[PositionSchema]

class PortfoliosSchema(BaseSchema):
    portfolios: list[PortfolioSchema]