import abc

from portfolio_manager.detabase import Database
from portfolio_manager.domain.models import Portfolio


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


class PortfolioRepository(AbstractPortfolioRepository):

    async def get_many(self, page: int | None = None, size: int | None = None) -> list[Portfolio]:
        ## TODO Add paging 
        return self.portfolios

    async def update_one(self, portfolio: Portfolio) -> bool:
        ## TODO implement
        pass

    def __init__(self, db: Database):
        self.portfolios = db.portfolios

    async def create_one(self, portfolio: Portfolio) -> bool:
        id_ = len(self.portfolios) + 1
        portfolio.id = id_
        self.portfolios.append(portfolio)
        return True

    async def get_one(self, id_: int) -> Portfolio | None:
        for portfolio in self.portfolios:
            if portfolio.id == id_:
                return portfolio
        return None
