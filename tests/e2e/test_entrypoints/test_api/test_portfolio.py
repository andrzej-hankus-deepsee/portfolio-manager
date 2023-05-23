from tests import BaseE2ETestCase


class TestExchangeFeed(BaseE2ETestCase):

    def test_create_portfolio(self):
        response = self.client.post(
            "/api/v1/portfolios",
            json={
                "name": 'portfolio-1',
                "cash": 100000.00,
                "positions": [
                    {
                        'symbol': 'AAPL',
                        'shares': 100,
                        'price': 10.00,
                    },
                    {
                        'symbol': 'CMG',
                        'shares': 50,
                        'price': 5.00,
                    }
                ]
            }
        )

        assert response.status_code == 201
        ## Check if tick recorded in database

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
                            'price': 10.00,
                        },
                        {
                            'symbol': 'CMG',
                            'shares': 50,
                            'price': 5.00,
                        }
                    ]
                }
            ]
        }
