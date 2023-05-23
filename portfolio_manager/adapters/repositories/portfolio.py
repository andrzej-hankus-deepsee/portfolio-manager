import abc

from portfolio_manager.domain.models import Portfolio


class AbstractPortfolioRepository(abc.ABC):
    @abc.abstractmethod
    async def create_one(self, portfolio: Portfolio) -> bool:
        raise NotImplementedError  # pragma: no cover

    @abc.abstractmethod
    async def get_one(self, id: int) -> Portfolio:
        raise NotImplementedError  # pragma: no cover

    @abc.abstractmethod
    async def get_many(self, page: int | None = None, size: int | None = None) -> list[Portfolio]:
        raise NotImplementedError  # pragma: no cover

    @abc.abstractmethod
    async def update_one(self, portfolio: Portfolio) -> bool:
        raise NotImplementedError  # pragma: no cover

    @abc.abstractmethod
    async def delete_one(self, id: int) -> bool:
        raise NotImplementedError  # pragma: no cover