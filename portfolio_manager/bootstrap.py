from functools import cached_property

from portfolio_manager.adapters.repositories import AbstractPortfolioRepository, PortfolioRepository, AbstractTickerRepository, TickerRepository
from portfolio_manager.detabase import Database

DATABSE = Database()


class Bootstrap:

    @cached_property
    def database(self) -> Database:
        return DATABSE

    @cached_property
    def portfolio_repository(self) -> AbstractPortfolioRepository:
        return PortfolioRepository(self.database)

    @cached_property
    def ticker_repository(self) -> AbstractTickerRepository:
        return TickerRepository(self.database)


def get_bootstrap():
    return Bootstrap()
