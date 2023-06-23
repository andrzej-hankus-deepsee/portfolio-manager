from portfolio_manager.domain.models import Position, Portfolio
from tests import BaseE2ETestCase


class TestExchangeFeed(BaseE2ETestCase):

    def test_create_portfolio(self):
        response = self.client.post(
            "/api/v1/portfolios",
            json={
                "name": 'portfolio-2',
                "cash": 100000.00,
                "positions": [
                    {
                        'shares': 100,
                        'ticker': {
                            'symbol': "AAPL",
                            'price': 100.0
                        }
                    },
                    {
                        'shares': 50,
                        'ticker': {
                            'symbol': "CMG",
                            'price': 50.0
                        }
                    }
                ]
            }
        )

        assert response.status_code == 201

        portfolios = self.bootstrap.database.portfolios

        tickers = self.bootstrap.database.tickers

        assert len(portfolios) == 2
        assert portfolios == [
            Portfolio(
                id=1,
                name='portfolio-1',
                cash=100000.00,
                positions=[
                    Position(
                        ticker=tickers[0],
                        shares=100,
                    ),
                    Position(
                        ticker=tickers[1],
                        shares=50,
                    )
                ]
            ),
            Portfolio(
                id=2,
                name='portfolio-2',
                cash=100000.00,
                positions=[
                    Position(
                        ticker=tickers[0],
                        shares=100,
                    ),
                    Position(
                        ticker=tickers[1],
                        shares=50,
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
                            'shares': 100,
                            'ticker': {
                                'symbol': "AAPL",
                                'price': 100.0
                            }
                        },
                        {
                            'shares': 50,
                            'ticker': {
                                'symbol': "CMG",
                                'price': 50.0
                            }
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
                    'shares': 100,
                    'ticker': {
                        'symbol': "AAPL",
                        'price': 100.0
                    }
                },
                {
                    'shares': 50,
                    'ticker': {
                        'symbol': "CMG",
                        'price': 50.0
                    }
                }
            ]
        }
