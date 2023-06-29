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
                        'buying_price': 90.0,
                        'shares': 100,
                        'ticker': {
                            'symbol': "AAPL",
                            'price': 100.0
                        }
                    },
                    {
                        'buying_price': 40.0,
                        'shares': 50,
                        'ticker': {
                            'symbol': "CMG",
                            'price': 50.0
                        }
                    }
                ],
                "orders": []
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
                        buying_price=90.0,
                        ticker=tickers[0],
                        shares=100,
                    ),
                    Position(
                        buying_price=40.0,
                        ticker=tickers[1],
                        shares=50,
                    )
                ],
                orders=[]
            ),
            Portfolio(
                id=2,
                name='portfolio-2',
                cash=100000.00,
                positions=[
                    Position(
                        buying_price=90.0,
                        ticker=tickers[0],
                        shares=100,
                    ),
                    Position(
                        buying_price=40.0,
                        ticker=tickers[1],
                        shares=50,
                    )
                ],
                orders=[]
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
                    'orders': [],
                    "positions": [
                        {
                            'buyingPrice': 90.0,
                            'shares': 100,
                            'ticker': {
                                'symbol': "AAPL",
                                'price': 100.0
                            }
                        },
                        {
                            'buyingPrice': 40.0,
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

    def test_get_portfolio_by_id(self):
        response = self.client.get(
            "/api/v1/portfolios/1"
        )

        assert response.status_code == 200
        assert response.json() == {
            "id": 1,
            "name": 'portfolio-1',
            "cash": 100000.00,
            'orders': [],
            "positions": [
                {
                    'buyingPrice': 90.0,
                    'shares': 100,
                    'ticker': {
                        'symbol': "AAPL",
                        'price': 100.0
                    }
                },
                {
                    'buyingPrice': 40.0,
                    'shares': 50,
                    'ticker': {
                        'symbol': "CMG",
                        'price': 50.0
                    }
                }
            ]
        }

    def test_price_change_in_portfolio(self):
        assert False
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
                        'price': 100.0,
                        'buyingPrice': 90.0
                    }
                },
                {
                    'shares': 50,
                    'ticker': {
                        'symbol': "CMG",
                        'price': 50.0,
                        'buyingPrice': 90.0
                    }
                }
            ]
        }

        response = self.client.patch(
            "/api/v1/tickers",
            json={
                "symbol": "AAPL",
                "price": 101.0,
            }
        )

        assert response.status_code == 201

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
                        'price': 101.0
                    },
                    'buyingPrice': 90.0
                },
                {
                    'shares': 50,
                    'ticker': {
                        'symbol': "CMG",
                        'price': 50.0
                    },
                    'buyingPrice': 90.0
                }
            ]
        }