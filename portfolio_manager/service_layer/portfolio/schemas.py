from portfolio_manager.shared.schemas import BaseSchema
from portfolio_manager.service_layer.ticker.schemas import LightTickerSchema, TickerSchema

class PositionSchema(BaseSchema):
    ticker: TickerSchema
    shares: int
    buying_price: float

class PositionOrderSchema(BaseSchema):
    ticker: LightTickerSchema
    shares: int
    max_price: float

class PortfolioSchema(BaseSchema):
    id : int | None = None
    name: str
    cash: float
    positions: list[PositionSchema]
    orders: list[PositionOrderSchema]

class CreatePortfolioSchema(BaseSchema):
    name: str
    cash: float
    positions: list[PositionSchema]
    orders: list[PositionOrderSchema]

class PortfoliosSchema(BaseSchema):
    portfolios: list[PortfolioSchema]

class OrderSchema(BaseSchema):
    portfolio_id : int 
    position_order : PositionOrderSchema