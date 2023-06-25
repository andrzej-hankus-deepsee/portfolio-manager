import abc

import datetime 

from portfolio_manager.detabase import Database
from portfolio_manager.domain.models import Ticker, TickerRecord


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
        self.records = db.tickers_records
    
    def record_tick(self, ticker):
        self.records.append(TickerRecord(symbol=ticker.symbol, price=ticker.price, time=datetime.datetime.now()))

    async def create_one(self, ticker: Ticker) -> bool:
        for tickers_local in self.tickers:
            if tickers_local.symbol == ticker.symbol:
                return False
            
        self.tickers.append(ticker)
        self.record_tick(ticker)
        return True

    async def get_one(self, symbol: int) -> Ticker | None:
        for ticker in self.tickers:
            if ticker.symbol == symbol:
                return ticker
        return None
    
    async def update_one(self, ticker: Ticker) -> bool:
        for tickers_local in self.tickers:
            if tickers_local.symbol == ticker.symbol:
                tickers_local.price = ticker.price
                self.record_tick(ticker)
                return True
        
        return False