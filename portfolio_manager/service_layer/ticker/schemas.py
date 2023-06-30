from portfolio_manager.shared.schemas import BaseSchema

class TickerSchema(BaseSchema):
    symbol: str
    price: float

class LightTickerSchema(BaseSchema):
    symbol: str

class TickersSchema(BaseSchema):
    tickers: list[TickerSchema]