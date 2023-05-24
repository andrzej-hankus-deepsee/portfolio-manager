from functools import cached_property

from portfolio_manager.adapters.repositories import AbstractPortfolioRepository, PortfolioRepository
from portfolio_manager.detabase import Database
from portfolio_manager.service_layer.messagebus import MessageBus

DATABSE = Database()


class Bootstrap:

    @cached_property
    def database(self) -> Database:
        return DATABSE

    @cached_property
    def portfolio_repository(self) -> AbstractPortfolioRepository:
        return PortfolioRepository(self.database)

    @cached_property
    def message_bus(self) -> MessageBus:
        return MessageBus()


def get_bootstrap():
    return Bootstrap()
