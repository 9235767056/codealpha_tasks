import csv

def stock_tracker():
    """
    A simple stock tracker that calculates total investment based on manually defined stock prices.
    """
    # Hardcoded dictionary for stock prices
    stock_prices = {
        "AAPL": 180.00,
        "TSLA": 250.00,
        "GOOGL": 150.00,
        "MSFT": 400.00,
        "AMZN": 190.00
    }

    portfolio = {}
    total_investment_value = 0.0

    print("Welcome to the Simple Stock Tracker!")
    print("Available stocks and their prices:")
    for ticker, price in stock_prices.items():
        print(f"  {ticker}: ${price:.2f}")

    while True:
        stock_name = input("\nEnter stock ticker (e.g., AAPL) or 'done' to finish: ").upper()
        if stock_name == 'DONE':
            break

        if stock_name not in stock_prices:
            print("Invalid stock ticker. Please choose from the available stocks.")
            continue

        while True:
            try:
                quantity = int(input(f"Enter quantity for {stock_name}: "))
                if quantity <= 0:
                    print("Quantity must be a positive number.")
                else:
                    break
            except ValueError:
                print("Invalid quantity. Please enter a whole number.")

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        print(f"Added {quantity} shares of {stock_name} to your portfolio.")

    print("\n--- Your Investment Summary ---")
    if not portfolio:
        print("Your portfolio is empty.")
    else:
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            total_investment_value += value
            print(f"{stock}: {quantity} shares @ ${price:.2f} = ${value:.2f}")

        print(f"\nTotal Investment Value: ${total_investment_value:.2f}")

    # Optional: Save the result to a file
    save_option = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
    if save_option == 'yes':
        file_type = input("Save as (txt/csv)? ").lower()
        if file_type == 'txt':
            file_name = "investment_summary.txt"
            with open(file_name, 'w') as f:
                f.write("--- Your Investment Summary ---\n")
                if not portfolio:
                    f.write("Your portfolio is empty.\n")
                else:
                    for stock, quantity in portfolio.items():
                        price = stock_prices[stock]
                        value = price * quantity
                        f.write(f"{stock}: {quantity} shares @ ${price:.2f} = ${value:.2f}\n")
                    f.write(f"\nTotal Investment Value: ${total_investment_value:.2f}\n")
            print(f"Summary saved to {file_name}")
        elif file_type == 'csv':
            file_name = "investment_summary.csv"
            with open(file_name, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Stock", "Quantity", "Price per Share", "Total Value"])
                if portfolio:
                    for stock, quantity in portfolio.items():
                        price = stock_prices[stock]
                        value = price * quantity
                        writer.writerow([stock, quantity, f"{price:.2f}", f"{value:.2f}"])
                writer.writerow([]) # Blank row for separation
                writer.writerow(["Total Investment Value", "", "", f"{total_investment_value:.2f}"])
            print(f"Summary saved to {file_name}")
        else:
            print("Invalid file type. Summary not saved.")

if __name__ == "__main__":
    stock_tracker()
