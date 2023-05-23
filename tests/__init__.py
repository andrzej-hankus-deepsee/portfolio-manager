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

    def setUp(self) -> None:
        self.client = TestClient(app=api)

    def normalize_dt_for_mongo(self, dt):
        return dt.replace(microsecond=1000 * (dt.microsecond // 1000))


class BaseE2ETestCase(BaseIntegrationTestCase):
    pass