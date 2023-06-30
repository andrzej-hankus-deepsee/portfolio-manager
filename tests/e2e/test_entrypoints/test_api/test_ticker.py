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
                symbol="APPL",
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
                symbol="APPL",
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
        tickers_records = self.bootstrap.database.tickers_records["APPL"]
        assert len(tickers) == 2
        assert tickers == [
            Ticker(
                symbol="APPL",
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
                "symbol": "APPL",
                "price": 101.0,
            }
        )

        assert response.status_code == 201

        assert len(tickers) == 2
        assert tickers == [
            Ticker(
                symbol="APPL",
                price=101.0,
            ),
            Ticker(
                symbol="CMG",
                price=50.0,
            )
        ]

        assert len(tickers_records) == records_lenght + 1
        
        tick_record = tickers_records[-1]

        assert tick_record.symbol == "APPL"
        assert tick_record.price == 101.0
        assert datetime.datetime.now() - tick_record.time < datetime.timedelta(seconds=5)
