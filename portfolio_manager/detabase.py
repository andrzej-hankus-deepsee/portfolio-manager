from functools import cached_property


class Database:

    def __init__(self):
        self.portfolios = []
        self.tickers = []
        self.tickers_records = {}

    @cached_property
    def portfolios(self):
        return self.portfolios

    @cached_property
    def tickers(self):
        return self.tickers

    def clean(self):
        self.portfolios = []
        self.tickers = []
