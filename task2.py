import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity
        print(f"Added {quantity} shares of {symbol} to the portfolio.")

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            if self.portfolio[symbol] >= quantity:
                self.portfolio[symbol] -= quantity
                if self.portfolio[symbol] == 0:
                    del self.portfolio[symbol]
                print(f"Removed {quantity} shares of {symbol} from the portfolio.")
            else:
                print(f"Not enough shares of {symbol} to remove.")
        else:
            print(f"{symbol} is not in the portfolio.")

    def track_portfolio(self):
        if not self.portfolio:
            print("Portfolio is empty.")
            return

        total_value = 0
        print("\nStock Portfolio Performance:")
        print("-" * 30)
        for symbol, quantity in self.portfolio.items():
            stock = yf.Ticker(symbol)
            stock_info = stock.history(period="1d")
            if not stock_info.empty:
                current_price = stock_info['Close'].iloc[-1]
                value = current_price * quantity
                total_value += value
                print(f"{symbol}: {quantity} shares | Current Price: ${current_price:.2f} | Total Value: ${value:.2f}")
            else:
                print(f"{symbol}: Data not available.")
        print("-" * 30)
        print(f"Total Portfolio Value: ${total_value:.2f}\n")

def main():
    portfolio = StockPortfolio()
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(symbol, quantity)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.remove_stock(symbol, quantity)
        elif choice == '3':
            portfolio.track_portfolio()
        elif choice == '4':
            print("Exiting the portfolio tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
