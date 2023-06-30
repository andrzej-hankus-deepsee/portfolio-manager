import abc

from portfolio_manager.detabase import Database
from portfolio_manager.domain.models import Portfolio, Ticker, PositionOrder
from fastapi import HTTPException

class AbstractPortfolioRepository(abc.ABC):
    @abc.abstractmethod
    async def create_one(self, portfolio: Portfolio) -> bool:
        raise NotImplementedError  # pragma: no cover

    @abc.abstractmethod
    async def get_one(self, id_: int) -> Portfolio:
        raise NotImplementedError  # pragma: no cover

    @abc.abstractmethod
    async def get_many(self, page: int | None = None, size: int | None = None) -> list[Portfolio]:
        raise NotImplementedError  # pragma: no cover

    @abc.abstractmethod
    async def add_postion_order(self, portfolio_id: int, position_order: PositionOrder) -> bool:
        raise NotImplementedError  # pragma: no cover

    @abc.abstractmethod
    async def respond_to_price_change(self, ticker: Ticker) -> bool:
        raise NotImplementedError  # pragma: no cover

class PortfolioRepository(AbstractPortfolioRepository):
    def __init__(self, db: Database):
        self.portfolios = db.portfolios
        self.tickers = db.tickers

    async def get_many(self, page: int | None = None, size: int | None = None) -> list[Portfolio]:
        ## TODO Add paging 
        return self.portfolios

    async def add_postion_order(self, portfolio_id: int, position_order: PositionOrder) -> bool:
        for portfolio in self.portfolios:
            if portfolio.id == portfolio_id:
                return portfolio.create_order(position_order.ticker, position_order.shares, position_order.max_price)
        raise HTTPException(status_code=404, detail="Portfolio not found")

    async def respond_to_price_change(self, ticker: Ticker) -> bool:
        for portfolio in self.portfolios:
            for position in portfolio.positions:
                if position.ticker.symbol == ticker.symbol:
                    position.ticker = ticker ## TODO if we would use database this sould not be a problem

                if position.ticker.symbol == ticker.symbol and ticker.price > 1.1 * position.buying_price:
                    percent_of_shares_to_sell = (((ticker.price/position.buying_price)-1.0)/2.0)
                    shares_to_sell = int(percent_of_shares_to_sell*position.shares)
                    if shares_to_sell <= 1:
                        shares_to_sell = 1
                    portfolio.sell(position, shares_to_sell)
            
            for position_order in portfolio.orders:
                if position_order.ticker.symbol == ticker.symbol:
                    position_order.ticker = ticker ## TODO if we would use database this sould not be a problem

                if position_order.ticker.symbol == ticker.symbol:
                    print(position_order.ticker.symbol)
                    print(ticker.price)
                    print(position_order.max_price)
                if position_order.ticker.symbol == ticker.symbol and ticker.price <= position_order.max_price:
                    portfolio.buy(position_order)

    async def create_one(self, portfolio: Portfolio) -> bool:
        id_ = len(self.portfolios) + 1
        args = portfolio.dict()
        args['id'] = id_
        portfolio_obj = Portfolio(**args)
        
        portfolio_obj.positions = list()
        for position in portfolio.positions:
            for ticker in self.tickers:
                if ticker.symbol == position.ticker.symbol:
                    position.ticker = ticker
                    portfolio_obj.positions.append(position)
                    break

        if len(portfolio_obj.positions) != len(portfolio.positions):
            return False
        
        self.portfolios.append(portfolio_obj)
        return True

    async def get_one(self, id_: int) -> Portfolio | None:
        result = None
        for portfolio in self.portfolios:
            if portfolio.id == id_:
                result = portfolio
                continue
        
        return result
