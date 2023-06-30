from tests import BaseE2ETestCase


class TestExchangeFeed(BaseE2ETestCase):

    def test_placing_order_buy_right_away(self):
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
                        'symbol': "APPL",
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

        response = self.client.post(
            "/api/v1/portfolios/order/",
            json={
                "portfolioId": 1,
                "positionOrder": {
                    "ticker": {
                    "symbol": "APPL"
                    },
                    "shares": 4,
                    "maxPrice": 150
                }
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
            "cash": 99600.00,
            'orders': [],
            "positions": [
                {
                    'buyingPrice': 90.0,
                    'shares': 100,
                    'ticker': {
                        'symbol': "APPL",
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
                },
                {
                    'buyingPrice': 100.0,
                    'shares': 4,
                    'ticker': {
                        'symbol': "APPL",
                        'price': 100.0
                    }
                }
            ]
        }

    def test_placing_order_buy_after_price_change(self):
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
                        'symbol': "APPL",
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

        response = self.client.post(
            "/api/v1/portfolios/order/",
            json={
                "portfolioId": 1,
                "positionOrder": {
                    "ticker": {
                    "symbol": "APPL"
                    },
                    "shares": 4,
                    "maxPrice": 90
                }
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
            "cash": 99640.00,
            'orders': [
                {
                    'maxPrice': 90.0,
                    'shares': 4,
                    'ticker': {
                        'symbol': "APPL"
                    }
                }
                ],
            "positions": [
                {
                    'buyingPrice': 90.0,
                    'shares': 100,
                    'ticker': {
                        'symbol': "APPL",
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

        response = self.client.patch(
            "/api/v1/tickers",
            json={
                "symbol": "APPL",
                "price": 89.0,
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
            "cash": 99644.00,
            'orders': [
                ],
            "positions": [
                {
                    'buyingPrice': 90.0,
                    'shares': 100,
                    'ticker': {
                        'symbol': "APPL",
                        'price': 89.0
                    }
                },
                {
                    'buyingPrice': 40.0,
                    'shares': 50,
                    'ticker': {
                        'symbol': "CMG",
                        'price': 50.0
                    }
                },
                {
                    'buyingPrice': 89.0,
                    'shares': 4,
                    'ticker': {
                        'symbol': "APPL",
                        'price': 89.0
                    }
                }
            ]
        }

    def test_placing_order_not_enough_cash(self):
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
                        'symbol': "APPL",
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

        response = self.client.post(
            "/api/v1/portfolios/order/",
            json={
                "portfolioId": 1,
                "positionOrder": {
                    "ticker": {
                    "symbol": "APPL"
                    },
                    "shares": 10000,
                    "maxPrice": 900
                }
            }
        )

        assert response.status_code == 400
        assert response.json() == {'detail': 'Order not created'}

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
                        'symbol': "APPL",
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

    def test_placing_order_price_too_high(self):
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
                        'symbol': "APPL",
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

        response = self.client.post(
            "/api/v1/portfolios/order/",
            json={
                "portfolioId": 1,
                "positionOrder": {
                    "ticker": {
                    "symbol": "APPL"
                    },
                    "shares": 4,
                    "maxPrice": 90
                }
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
            "cash": 99640.00,
            'orders': [
                {
                    'maxPrice': 90.0,
                    'shares': 4,
                    'ticker': {
                        'symbol': "APPL"
                    }
                }
                ],
            "positions": [
                {
                    'buyingPrice': 90.0,
                    'shares': 100,
                    'ticker': {
                        'symbol': "APPL",
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

        response = self.client.patch(
            "/api/v1/tickers",
            json={
                "symbol": "APPL",
                "price": 91.0,
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
            "cash": 99640.00,
            'orders': [
                {
                    'maxPrice': 90.0,
                    'shares': 4,
                    'ticker': {
                        'symbol': "APPL"
                    }
                }
                ],
            "positions": [
                {
                    'buyingPrice': 90.0,
                    'shares': 100,
                    'ticker': {
                        'symbol': "APPL",
                        'price': 91.0
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
