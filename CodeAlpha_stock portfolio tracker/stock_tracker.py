stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 350
}

total = 0

stock = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if stock in stock_prices:
    total = stock_prices[stock] * quantity
    print("Total Investment Value =", total)
else:
    print("Stock not found")