from portfolio_manager.shared.schemas import BaseSchema

class TickerSchema(BaseSchema):
    id : int | None = None
    symbol: str
    price: float