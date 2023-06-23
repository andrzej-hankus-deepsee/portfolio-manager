from portfolio_manager.domain.models import Position, Portfolio, Ticker
from tests import BaseE2ETestCase


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

    def test_create_portfolio(self):
        response = self.client.post(
            "/api/v1/portfolios",
            json={
                "name": 'portfolio-2',
                "cash": 100000.00,
                "positions": [
                    {
                        'symbol': 'AAPL',
                        'shares': 100,
                    },
                    {
                        'symbol': 'CMG',
                        'shares': 50,
                    }
                ]
            }
        )

        assert response.status_code == 201

        portfolios = self.bootstrap.database.portfolios
        assert len(portfolios) == 2
        assert portfolios == [
            Portfolio(
                id=1,
                name='portfolio-1',
                cash=100000.00,
                positions=[
                    Position(
                        symbol='AAPL',
                        shares=100,
                        price=10.00,
                    ),
                    Position(
                        symbol='CMG',
                        shares=50,
                        price=5.00,
                    )
                ]
            ),
            Portfolio(
                id=2,
                name='portfolio-2',
                cash=100000.00,
                positions=[
                    Position(
                        symbol='AAPL',
                        shares=100,
                        price=10.00,
                    ),
                    Position(
                        symbol='CMG',
                        shares=50,
                        price=5.00,
                    )
                ]
            )
        ]

    def test_get_portfolios(self):
        response = self.client.get(
            "/api/v1/portfolios"
        )

        assert response.status_code == 200
        assert response.json() == {
            "portfolios": [
                {
                    "id": 1,
                    "name": 'portfolio-1',
                    "cash": 100000.00,
                    "positions": [
                        {
                            'symbol': 'AAPL',
                            'shares': 100,
                            'price': 100 * 100.0,
                        },
                        {
                            'symbol': 'CMG',
                            'shares': 50,
                            'price': 50 * 50.0,
                        }
                    ]
                }
            ]
        }

    def test_get_portfolio__by_id(self):
        response = self.client.get(
            "/api/v1/portfolios/1"
        )

        assert response.status_code == 200
        assert response.json() == {
            "id": 1,
            "name": 'portfolio-1',
            "cash": 100000.00,
            "positions": [
                {
                    'symbol': 'AAPL',
                    'shares': 100,
                    'price': 100 * 100.0
                },
                {
                    'symbol': 'CMG',
                    'shares': 50,
                    'price': 50 * 50.0,
                }
            ]
        }
