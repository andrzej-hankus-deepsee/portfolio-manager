from unittest import IsolatedAsyncioTestCase

import pytest
from fastapi.testclient import TestClient
from pytest_mock import MockerFixture

from portfolio_manager.bootstrap import Bootstrap
from portfolio_manager.entrypoints.api import api
from portfolio_manager.domain.models import Position, Portfolio, Ticker

class BaseIntegrationTestCase(IsolatedAsyncioTestCase):
    @pytest.fixture(scope="function", autouse=True)
    def init_fixtures(
        self,
        mocker: MockerFixture,
    ):
        self.mocker = mocker
        self.bootstrap = Bootstrap()
        yield
        self.bootstrap.database.clean()

    def setUp(self) -> None:
        self.client = TestClient(app=api)
        
        self.bootstrap.database.tickers = [
            Ticker(
                id=1,
                symbol="APPL",
                price=100.0,
            ),
            Ticker(
                id=2,
                symbol="CMG",
                price=50.0,
            )
        ]
        tickers = self.bootstrap.database.tickers
        self.bootstrap.database.portfolios = [
            Portfolio(
                id=1,
                name='portfolio-1',
                cash=100000.00,
                positions=[
                    Position(
                        ticker=tickers[0],
                        shares=100,
                        buying_price=90.0,
                    ),
                    Position(
                        ticker=tickers[1],
                        shares=50,
                        buying_price=40.0,
                    )
                ],
                orders=[]
            )
        ]


class BaseE2ETestCase(BaseIntegrationTestCase):
    pass