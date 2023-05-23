from tests import BaseE2ETestCase


class TestExchangeFeed(BaseE2ETestCase):

    def test_create_tick(self):
        response = self.client.post(
            "/api/v1/tickers",
            json={
                "symbol": "AAPL",
                "price": 100.0,
            }
        )

        assert response.status_code == 201
        ## Check if tick recorded in database

    def test_create_tick__with_significant_gain_for_stock_in_portfolio(self):
        response = self.client.post(
            "/api/v1/tickers",
            json={
                "symbol": "AAPL",
                "price": 100.0,
            }
        )

        assert response.status_code == 201
        ## Check if tick recorded in database
        ## Check if portfolio updated with new value
