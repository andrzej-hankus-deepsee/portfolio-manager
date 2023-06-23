from tests import BaseE2ETestCase
from portfolio_manager.domain.models import Position, Portfolio, Ticker

class TestExchangeFeed(BaseE2ETestCase):
    def setUp(self):
        super().setUp()

        self.bootstrap.database.tickers = [
            Ticker(
                id=1,
                symbol="AAPL",
                price=100.0,
            ),
            Ticker(
                id=2,
                symbol="CMG",
                price=50.0,
            )
        ]

        self.bootstrap.database.portfolios = [
            Portfolio(
                id=1,
                name='portfolio-1',
                cash=100000.00,
                positions=[
                    Position(
                        symbol='AAPL',
                        shares=100,
                    ),
                    Position(
                        symbol='CMG',
                        shares=50,
                    )
                ]
            )
        ]


    def test_create_tick(self):
        response = self.client.post(
            "/api/v1/tickers",
            json={
                "symbol": "TEST",
                "price": 100.0,
            }
        )

        assert response.status_code == 201

        tickers = self.bootstrap.database.tickers
        assert len(tickers) == 3
        assert tickers == [
            Ticker(
                id=1,
                symbol="AAPL",
                price=100.0,
            ),
            Ticker(
                id=2,
                symbol="CMG",
                price=50.0,
            ),
            Ticker(
                id=3,
                symbol="TEST",
                price=100.0,
            )
        ]


    def test_create_tick_with_significant_gain_for_stock_in_portfolio(self):
        ticker_symbol = "AAPL"
        ticker_price_before_test = 100.0
        ticker_price_after_test = 101.0


        test_portfolio = self.bootstrap.database.portfolios[0]

        for position in test_portfolio.positions:
            if position.symbol == ticker_symbol:
                assert position.price == ticker_price_before_test*position.shares

        response = self.client.post(
            "/api/v1/tickers",
            json={
                "symbol": ticker_symbol,
                "price": ticker_price_after_test,
            }
        )

        assert response.status_code == 201
        
        ## TODO Check if tick recorded in database
        for position in test_portfolio.positions:
            if position.symbol == ticker_symbol:
                assert position.price == ticker_price_after_test*position.shares
