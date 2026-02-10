import requests

class BinanceMonitor:
    def __init__(self):
        self.base_url = 'https://api.binance.com/api/v3'

    def get_exchange_info(self):
        response = requests.get(f'{self.base_url}/exchangeInfo')
        return response.json()

    def get_ticker_data(self, symbol):
        response = requests.get(f'{self.base_url}/ticker/price?symbol={symbol}')
        return response.json()

# Example usage:
if __name__ == '__main__':
    monitor = BinanceMonitor()
    print(monitor.get_exchange_info())
    print(monitor.get_ticker_data('BTCUSDT'))