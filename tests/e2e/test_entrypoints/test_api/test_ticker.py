from tests import BaseE2ETestCase
from portfolio_manager.domain.models import Ticker, TickerRecord
import datetime
class TestExchangeFeed(BaseE2ETestCase):

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
        tickers_records = self.bootstrap.database.tickers
        assert len(tickers) == 3
        assert tickers == [
            Ticker(
                symbol="AAPL",
                price=100.0,
            ),
            Ticker(
                symbol="CMG",
                price=50.0,
            ),
            Ticker(
                symbol="TEST",
                price=100.0,
            )
        ]
    
    def test_create_tick_failed(self):
        response = self.client.post(
            "/api/v1/tickers",
            json={
                "symbol": "TEST",
                "price": 100.0,
            }
        )

        assert response.status_code == 201

        response = self.client.post(
            "/api/v1/tickers",
            json={
                "symbol": "TEST",
                "price": 100.0,
            }
        )

        assert response.status_code == 409

        tickers = self.bootstrap.database.tickers

        assert len(tickers) == 3
        assert tickers == [
            Ticker(
                symbol="AAPL",
                price=100.0,
            ),
            Ticker(
                symbol="CMG",
                price=50.0,
            ),
            Ticker(
                symbol="TEST",
                price=100.0,
            )
        ]

    def test_tick_recording(self):

        tickers = self.bootstrap.database.tickers
        tickers_records = self.bootstrap.database.tickers_records["AAPL"]
        assert len(tickers) == 2
        assert tickers == [
            Ticker(
                symbol="AAPL",
                price=100.0,
            ),
            Ticker(
                symbol="CMG",
                price=50.0,
            )
        ]

        records_lenght = len(tickers_records)

        response = self.client.patch(
            "/api/v1/tickers",
            json={
                "symbol": "AAPL",
                "price": 101.0,
            }
        )

        assert response.status_code == 201

        assert len(tickers) == 2
        assert tickers == [
            Ticker(
                symbol="AAPL",
                price=101.0,
            ),
            Ticker(
                symbol="CMG",
                price=50.0,
            )
        ]

        assert len(tickers_records) == records_lenght + 1
        
        tick_record = tickers_records[-1]

        assert tick_record.symbol == "AAPL"
        assert tick_record.price == 101.0
        assert datetime.datetime.now() - tick_record.time < datetime.timedelta(seconds=5)


    def test_create_tick_with_significant_gain_for_stock_in_portfolio(self):
        ticker_symbol = "AAPL"
        ticker_price_before_gain = 100.0
        ticker_price_after_gain = 150.0


        test_portfolio = self.bootstrap.database.portfolios[0]

        response = self.client.patch(
            "/api/v1/tickers",
            json={
                "symbol": ticker_symbol,
                "price": ticker_price_after_gain,
            }
        )

        assert response.status_code == 201
        
        ## TODO Check if tick recorded in database
        ## TODO Check if tick triggered an action 
