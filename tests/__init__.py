from unittest import IsolatedAsyncioTestCase

import pytest
from fastapi.testclient import TestClient
from pytest_mock import MockerFixture

from portfolio_manager.bootstrap import Bootstrap
from portfolio_manager.entrypoints.api import api


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


class BaseE2ETestCase(BaseIntegrationTestCase):
    pass