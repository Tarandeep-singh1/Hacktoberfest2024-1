import requests
import datetime

class BitcoinAnalyzer:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self):
        try:
            response = requests.get(self.api_url)
            if response.status_code == 200:
                data = response.json()
                return data['bpi']['USD']['rate_float']
            else:
                print("Error fetching data.")
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def analyze_price(self, current_price, past_price):
        if current_price > past_price:
            print(f"Bitcoin price has increased by {current_price - past_price:.2f} USD since last check.")
        elif current_price < past_price:
            print(f"Bitcoin price has decreased by {past_price - current_price:.2f} USD since last check.")
        else:
            print("Bitcoin price remains the same as last check.")

def main():
    bitcoin_api_url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    analyzer = BitcoinAnalyzer(bitcoin_api_url)

    # Simulate the last fetched price for comparison (in a real scenario, you'd store this)
    last_price = 25000.00
    
    current_price = analyzer.fetch_data()
    
    if current_price:
        print(f"Current Bitcoin Price (USD): {current_price:.2f}")
        analyzer.analyze_price(current_price, last_price)
        
        # Log the current price with timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Price logged at {timestamp}")

if __name__ == "__main__":
    main()
