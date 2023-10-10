class Balance:
    def __init__(self, currency, amount, precision):
        self.currency = currency
        self.amount = amount
        self.precision = precision

class Legal:
    def __init__(self, legal):
        self.legal = legal

class Crypto(Balance, Legal):
    def __init__(self, currency, amount, precision, url):
        super().__init__(currency, amount, precision)
        self.url = url
        self.legal="Legal text about bitcoin"
    def __str__(self):
        return f"{self.amount} {self.currency} with precision {self.precision} identitifed by {self.url}"


c = Crypto("BTC", 100, 2, "btc://wallet:12331khkh1khk1h23")

print(c)
print(c.legal)