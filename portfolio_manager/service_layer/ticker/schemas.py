from portfolio_manager.shared.schemas import BaseSchema

class TickerSchema(BaseSchema):
    symbol: str
    price: float