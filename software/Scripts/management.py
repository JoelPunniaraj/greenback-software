import sqlite3
import yfinance as yf
from prettytable import PrettyTable as pt
import locale
import pyfiglet

locale.setlocale(locale.LC_ALL, '')

conn = sqlite3.connect('portfolio.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS portfolio
             (ticker TEXT, shares INTEGER, cost_basis REAL)''')

def add_position(ticker, shares, cost_basis):
    c.execute("INSERT INTO portfolio VALUES (?, ?, ?)", (ticker, shares, cost_basis))
    conn.commit()

def get_live_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        return round(stock.history(period="1d").iloc[-1]['Close'], 2)
    except Exception as e:
        print(f"Error getting live price for {ticker}: {e}")
        return None

def is_valid_ticker(ticker):
    try:
        yf.Ticker(ticker).info
        return True
    except Exception:
        return False

def calculate_portfolio_value():
    total_value = 0
    c.execute("SELECT * FROM portfolio")
    rows = c.fetchall()
    for row in rows:
        ticker, shares, cost_basis = row
        live_price = get_live_price(ticker)
        if live_price is not None:
            position_value = shares * live_price
            total_value += position_value
    return total_value

def print_portfolio_table():

    sort_table = input("Do you want to sort the table first? (yes/no): ").lower()

    if sort_table == 'yes':
        while True:
            print("Sort Options:")
            print("- Sort by Value")
            print("- Sort by Profit")
            print("- Exit")
            print()
            sort_choice = input("Enter your sort choice: ").lower()
            
            if sort_choice == 'value':
                sort_key = lambda row: (row[1] * get_live_price(row[0])) if get_live_price(row[0]) is not None else 0
                reverse_sort = True
                break
            elif sort_choice == 'profit':
                sort_key = lambda row: row[6]
                reverse_sort = True
                break
            elif sort_choice == 'exit':
                return
            else:
                print("Invalid choice. Please enter a valid sort option.")
    else:
        sort_key = None
        reverse_sort = None

    table = pt(["Ticker", "Shares", "Cost Basis", "Initial Investment", "Current Price", "Position Value", "Profit/Loss", "% Change"])
    
    table.align["Ticker"] = "l"  
    table.align["Shares"] = "r"  
    table.align["Cost Basis"] = "r"  
    table.align["Initial Investment"] = "r" 
    table.align["Current Price"] = "r"  
    table.align["Position Value"] = "r" 
    table.align["Profit/Loss"] = "r" 
    table.align["% Change"] = "r" 
    
    c.execute("SELECT * FROM portfolio")
    rows = c.fetchall()
    
    if sort_key:
        sorted_rows = sorted(rows, key=sort_key, reverse=reverse_sort)
    else:
        sorted_rows = rows
        
    for row in sorted_rows:
        ticker, shares, cost_basis = row
        if ticker in ['BRKB', 'BRK.B']:
            continue
        live_price = get_live_price(ticker)
        if live_price is not None:
            position_value = shares * live_price
            initial_investment = shares * cost_basis
            profit_loss = position_value - initial_investment
            percent_change = ((live_price - cost_basis) / cost_basis) * 100 if cost_basis != 0 else 0
            formatted_cost_basis = locale.currency(cost_basis, grouping=True)
            formatted_live_price = locale.currency(live_price, grouping=True)
            formatted_position_value = locale.currency(position_value, grouping=True)
            formatted_initial_investment = locale.currency(initial_investment, grouping=True)
            formatted_profit_loss = locale.currency(profit_loss, grouping=True)
            formatted_percent_change = f"{percent_change:.2f}%"
            table.add_row([ticker, shares, formatted_cost_basis, formatted_initial_investment, 
            formatted_live_price, formatted_position_value, formatted_profit_loss, 
            formatted_percent_change])

    print(table)

    total_value = calculate_portfolio_value()
    formatted_total_value = locale.currency(total_value, grouping=True)
    print(f"\nTotal Value: {formatted_total_value}")
    print(f"\nTotal Profit: {formatted_total_value}")

def main_menu():

    ascii_banner1 = pyfiglet.figlet_format("D A T A S P R I N T", font="small")
    ascii_banner2 = pyfiglet.figlet_format("S O F T W A R E", font="small")
    print(ascii_banner1)
    print(ascii_banner2)

    while True:
        print("\nOptions:")
        print("- 'Add' - Add Position")
        print("- 'View' - View Portfolio")
        print("- 'Edit' - Edit a Position")
        print("- 'Remove' - Remove a Position")
        print("-  Exit")
        print()
        choice = input("Enter your choice: ").lower()
        if choice == 'add':
            add_position_menu()
        elif choice == 'view':
            print_portfolio_table()
        elif choice == 'edit':
            edit_position_menu()
        elif choice == 'remove':
            remove_position_menu()
        elif choice == 'exit':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def remove_position_menu():
    ticker = input("Enter the ticker symbol to remove: ").upper()
    c.execute("SELECT * FROM portfolio WHERE ticker=?", (ticker,))
    position = c.fetchone()
    if position is None:
        print("Position not found.")
    else:
        confirm = input(f"Do you want to remove {ticker} from the portfolio? (yes/no): ").lower()
        if confirm == 'yes':
            c.execute("DELETE FROM portfolio WHERE ticker=?", (ticker,))
            conn.commit()
            print(f"Position {ticker} removed successfully.")
        else:
            print("Operation canceled.")

def add_position_menu():
    while True:
        ticker = input("Enter the ticker symbol: ").upper()
        if is_valid_ticker(ticker):
            break
        else:
            print("Invalid ticker symbol. Please enter a valid ticker.")

    shares = int(input("Enter the number of shares: "))
    cost_basis = float(input("Enter the cost basis per share: "))
    add_position(ticker, shares, cost_basis)
    print("Position added successfully.")

def edit_position_menu():
    ticker = input("Enter the ticker symbol to edit: ").upper()
    c.execute("SELECT * FROM portfolio WHERE ticker=?", (ticker,))
    position = c.fetchone()
    if position is None:
        print("Position not found.")
    else:
        print("Current position:", position)
        new_shares = int(input("Enter the new number of shares (or leave empty to skip): ") or position[1])
        new_cost_basis = float(input("Enter the new cost basis per share (or leave empty to skip): ") or position[2])
        c.execute("UPDATE portfolio SET shares=?, cost_basis=? WHERE ticker=?", (new_shares, new_cost_basis, ticker))
        conn.commit()
        print("Position updated successfully.")

def get_live_price(ticker):
    try:
        if ticker in ['BRKB', 'BRK.B']:
            return None 
        stock = yf.Ticker(ticker)
        history = stock.history(period="1d")
        if not history.empty:
            return round(history.iloc[-1]['Close'], 2)
        else:
            return None
    except Exception as e:
        print(f"Error getting live price for {ticker}: {e}")
        return None

def is_valid_ticker(ticker):
    try:
        info = yf.Ticker(ticker).info
        if info:
            return True
        else:
            print(f"Invalid ticker symbol: {ticker}")
            return False
    except Exception as e:
        print(f"Error checking ticker symbol {ticker}: {e}")
        return False

if __name__ == "__main__":
    main_menu()
conn.close()
