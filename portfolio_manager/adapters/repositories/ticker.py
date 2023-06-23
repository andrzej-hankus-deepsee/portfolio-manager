import abc

from portfolio_manager.detabase import Database
from portfolio_manager.domain.models import Ticker


class AbstractTickerRepository(abc.ABC):
    @abc.abstractmethod
    async def create_one(self, Ticker: Ticker) -> bool:
        raise NotImplementedError  # pragma: no cover

    @abc.abstractmethod
    async def get_one(self, id_: int) -> Ticker:
        raise NotImplementedError  # pragma: no cover

    @abc.abstractmethod
    async def update_one(self, Ticker: Ticker) -> bool:
        raise NotImplementedError  # pragma: no cover


class TickerRepository(AbstractTickerRepository):
    async def update_one(self, Ticker: Ticker) -> bool:
        ## TODO implement
        pass

    def __init__(self, db: Database):
        self.Tickers = db.Tickers

    async def create_one(self, Ticker: Ticker) -> bool:
        id_ = len(self.Tickers) + 1
        Ticker.id = id_
        self.Tickers.append(Ticker)
        return True

    async def get_one(self, id_: int) -> Ticker | None:
        for Ticker in self.Tickers:
            if Ticker.id == id_:
                return Ticker
        return None
