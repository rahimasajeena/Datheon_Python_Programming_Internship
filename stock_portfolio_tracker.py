portfolio = []

print("=== Stock Portfolio Tracker ===")

while True:
    ticker = input("\nEnter stock ticker (or 'done' to finish): ").strip().upper()

    if ticker == "DONE":
        break

    if not ticker:
        print("Ticker cannot be empty.")
        continue

    try:
        shares = float(input("Enter number of shares: "))
        purchase_price = float(input("Enter purchase price per share: "))
        current_price = float(input("Enter current price per share: "))

        if shares <= 0 or purchase_price < 0 or current_price < 0:
            print("Please enter positive shares and non-negative prices.")
            continue

    except ValueError:
        print("Please enter valid numbers.")
        continue

    investment = shares * purchase_price
    current_value = shares * current_price
    profit_loss = current_value - investment

    stock = {
        "ticker": ticker,
        "shares": shares,
        "investment": investment,
        "current_value": current_value,
        "profit_loss": profit_loss
    }

    portfolio.append(stock)
    print(f"{ticker} added successfully!")

print("\n=== Portfolio Summary ===")

if not portfolio:
    print("No stocks were added.")
else:
    total_investment = 0
    total_value = 0

    for stock in portfolio:
        print(f"\nStock: {stock['ticker']}")
        print(f"Shares: {stock['shares']:g}")
        print(f"Investment: Rs. {stock['investment']:.2f}")
        print(f"Current Value: Rs. {stock['current_value']:.2f}")
        print(f"Profit/Loss: Rs. {stock['profit_loss']:.2f}")

        total_investment += stock["investment"]
        total_value += stock["current_value"]

    print("\n=== Overall Totals ===")
    print(f"Total Investment: Rs. {total_investment:.2f}")
    print(f"Total Current Value: Rs. {total_value:.2f}")
    print(f"Total Profit/Loss: Rs. {total_value - total_investment:.2f}")