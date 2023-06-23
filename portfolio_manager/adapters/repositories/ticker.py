import abc

from portfolio_manager.detabase import Database
from portfolio_manager.domain.models import Ticker


class AbstractTickerRepository(abc.ABC):
    @abc.abstractmethod
    async def create_one(self, ticker: Ticker) -> bool:
        raise NotImplementedError  # pragma: no cover

    @abc.abstractmethod
    async def get_one(self, id_: int) -> Ticker:
        raise NotImplementedError  # pragma: no cover

    @abc.abstractmethod
    async def update_one(self, ticker: Ticker) -> bool:
        raise NotImplementedError  # pragma: no cover


class TickerRepository(AbstractTickerRepository):
    def __init__(self, db: Database):
        self.tickers = db.tickers

    async def create_one(self, ticker: Ticker) -> bool:
        self.tickers.append(ticker)
        return True

    async def get_one(self, symbol: int) -> Ticker | None:
        for tickers in self.tickers:
            if tickers.symbol == symbol:
                return tickers
        return None
    
    async def update_one(self, ticker: Ticker) -> bool:
        ## TODO implement
        pass