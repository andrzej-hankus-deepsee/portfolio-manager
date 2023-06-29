import abc

from portfolio_manager.detabase import Database
from portfolio_manager.domain.models import Portfolio, Ticker


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
    async def update_one(self, portfolio: Portfolio) -> bool:
        raise NotImplementedError  # pragma: no cover

    @abc.abstractmethod
    async def respond_to_price_change(self, ticker: Ticker) -> bool:
        raise NotImplementedError  # pragma: no cover

class PortfolioRepository(AbstractPortfolioRepository):
    def __init__(self, db: Database):
        self.portfolios = db.portfolios

    async def get_many(self, page: int | None = None, size: int | None = None) -> list[Portfolio]:
        ## TODO Add paging 
        return self.portfolios

    async def update_one(self, portfolio: Portfolio) -> bool:
        ## TODO implement
        pass

    async def respond_to_price_change(self, ticker: Ticker) -> bool:
        for portfolio in self.portfolios:
            for position in portfolio.positions:
                if position.symbol == ticker.symbol and ticker.price > 1.1 * position.buying_price:
                    shares_to_sell = int((((position.buying_price/ticker.price)-1)/2)*position.shares)
                    if shares_to_sell <= 1:
                        shares_to_sell = 1
                    portfolio.sell(position, position.shares*.5)

    async def create_one(self, portfolio: Portfolio) -> bool:
        id_ = len(self.portfolios) + 1
        portfolio.id = id_
        portfolio = Portfolio(**portfolio.dict())
        self.portfolios.append(portfolio)
        return True

    async def get_one(self, id_: int) -> Portfolio | None:
        result = None
        for portfolio in self.portfolios:
            if portfolio.id == id_:
                result = portfolio
                continue
        
        return result
