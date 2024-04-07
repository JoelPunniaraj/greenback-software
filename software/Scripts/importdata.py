import os
import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from openpyxl.styles import Alignment
from openpyxl.workbook.workbook import Workbook

income_workbook_path = r"C:\Users\joelp\greenback\model\model.xlsx"
income_sheet_name = "income-sheet"
income_mapping = {
    "Revenue": 4,
    "Revenue Growth (YoY)": 5,
    "Cost of Revenue": 6,
    "Gross Profit": 7,
    "Selling, General & Admin": 8,
    "Research & Development": 9,
    "Operating Expenses": 10,
    "Operating Income": 11,
    "Interest Expense / Income": 12,
    "Other Expense / Income": 13,
    "Pretax Income": 14,
    "Income Tax": 15,
    "Net Income": 16,
    "Net Income Growth": 17,
    "Shares Outstanding (Basic)": 18,
    "Shares Outstanding (Diluted)": 19,
    "Shares Change": 20,
    "EPS (Basic)": 21,
    "EPS (Diluted)": 22,
    "EPS Growth": 23,
    "Free Cash Flow": 24,
    "Free Cash Flow Per Share": 25,
    "Dividend Per Share": 26,
    "Dividend Growth": 27,
    "Gross Margin": 28,
    "Operating Margin": 29,
    "Profit Margin": 30,
    "Free Cash Flow Margin": 31,
    "Effective Tax Rate": 32,
    "EBITDA": 33,
    "EBITDA Margin": 34,
    "Depreciation & Amortization": 35,
    "EBIT": 36,
    "EBIT Margin": 37
}

balance_workbook_path = r"C:\Users\joelp\greenback\model\model.xlsx"
balance_sheet_name = "balance-sheet"
balance_mapping = {
    "Cash & Equivalents": 4,
    "Short-Term Investments": 5,
    "Cash & Cash Equivalents": 6,
    "Cash Growth": 7,
    "Receivables": 8,
    "Inventory": 9,
    "Other Current Assets": 10,
    "Total Current Assets": 11,
    "Property, Plant & Equipment": 12,
    "Long-Term Investments": 13,
    "Goodwill and Intangibles": 14,
    "Other Long-Term Assets": 15,
    "Total Long-Term Assets": 16,
    "Total Assets": 17,
    "Accounts Payable": 18,
    "Deferred Revenue": 19,
    "Current Debt": 20,
    "Other Current Liabilities": 21,
    "Total Current Liabilities": 22,
    "Long-Term Debt": 23,
    "Other Long-Term Liabilities": 24,
    "Total Long-Term Liabilities": 25,
    "Total Liabilities": 26,
    "Total Debt": 27,
    "Debt Growth": 28,
    "Retained Earnings": 29, 
    "Comprehensive Income": 30,
    "Shareholders' Equity": 31,
    "Net Cash / Debt": 32,
    "Net Cash / Debt Growth": 33,
    "Net Cash Per Share": 34,
    "Working Capital": 35,
    "Book Value Per Share": 36
}

cash_flow_workbook_path = r"C:\Users\joelp\greenback\model\model.xlsx"
cash_flow_sheet_name = "cash-flow-sheet"
cash_flow_mapping = {
    "Net Income": 4,
    "Depreciation & Amortization": 5,
    "Share-Based Compensation": 6,
    "Other Operating Activities": 7, 
    "Operating Cash Flow": 8, 
    "Operating Cash Flow Growth": 9, 
    "Capital Expenditures": 10, 
    "Acquisitions": 11, 
    "Change in Investments": 12, 
    "Other Investing Activities": 13, 
    "Investing Cash Flow": 14, 
    "Dividends Paid": 15,
    "Share Issuance / Repurchase": 16, 
    "Debt Issued / Paid": 17,
    "Other Financing Activities": 18,
    "Financing Cash Flow": 19, 
    "Exchange Rate Effect": 20,
    "Net Cash Flow": 21,
    "Free Cash Flow": 22,
    "Free Cash Flow Growth": 23,
    "Free Cash Flow Margin": 24, 
    "Free Cash Flow Per Share": 25
}

market_cap_workbook_path = r"C:\Users\joelp\greenback\model\model.xlsx"
market_cap_sheet_name = "stock-history"
market_cap_mapping = {
    "Market Capitalization": 4,
    "Market Cap Growth": 5,
    "Enterprise Value": 6,
}

def import_income(url, income_mapping, income_workbook_path, income_sheet_name):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("tbody")
        rows = table.find_all("tr")    
        if not os.path.exists(income_workbook_path):
            workbook = Workbook()
        else:
            workbook = load_workbook(income_workbook_path)
        if income_sheet_name not in workbook.sheetnames:
            workbook.create_sheet(income_sheet_name)
        sheet = workbook[income_sheet_name]
        for row in rows:
            cells = row.find_all("td")
            metric = cells[0].get_text(strip=True)
            if metric in income_mapping:
                row_num = income_mapping[metric]
                values = [cell.get_text(strip=True) for cell in cells[1:21]] 
                for i, value in enumerate(values):
                    cell = sheet.cell(row=row_num, column=i+2)
                    cell.value = value
                    cell.alignment = Alignment(horizontal='right') 
        workbook.save(income_workbook_path)
        print("Income Sheet Data from 'stockanalysis.com' Added to Excel File Successfully!")
    else:
        print("Failed to Fetch Data from the Website!")

def import_balance(url, balance_mapping, balance_workbook_path, balance_sheet_name):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("tbody")
        rows = table.find_all("tr")    
        if not os.path.exists(balance_workbook_path):
            workbook = Workbook()
        else:
            workbook = load_workbook(balance_workbook_path)
        if balance_sheet_name not in workbook.sheetnames:
            workbook.create_sheet(balance_sheet_name)
        sheet = workbook[balance_sheet_name]
        for row in rows:
            cells = row.find_all("td")
            metric = cells[0].get_text(strip=True)
            if metric in balance_mapping:
                row_num = balance_mapping[metric]
                values = [cell.get_text(strip=True) for cell in cells[1:21]] 
                for i, value in enumerate(values):
                    cell = sheet.cell(row=row_num, column=i+2)
                    cell.value = value
                    cell.alignment = Alignment(horizontal='right') 
        workbook.save(balance_workbook_path)
        print("Balance Sheet Data from 'stockanalysis.com' Added to Excel File Successfully!")
    else:
        print("Failed to Fetch Data from the Website!")

def import_cash_flow(url, cash_flow_mapping, cash_flow_workbook_path, cash_flow_sheet_name):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("tbody")
        rows = table.find_all("tr")    
        if not os.path.exists(cash_flow_workbook_path):
            workbook = Workbook()
        else:
            workbook = load_workbook(cash_flow_workbook_path)
        if cash_flow_sheet_name not in workbook.sheetnames:
            workbook.create_sheet(cash_flow_sheet_name)
        sheet = workbook[cash_flow_sheet_name]
        for row in rows:
            cells = row.find_all("td")
            metric = cells[0].get_text(strip=True)
            if metric in cash_flow_mapping:
                row_num = cash_flow_mapping[metric]
                values = [cell.get_text(strip=True) for cell in cells[1:21]] 
                for i, value in enumerate(values):
                    cell = sheet.cell(row=row_num, column=i+2)
                    cell.value = value
                    cell.alignment = Alignment(horizontal='right') 
        workbook.save(cash_flow_workbook_path)
        print("Cash Flow Sheet Data from 'stockanalysis.com' Added to Excel File Successfully!")
    else:
        print("Failed to Fetch Data from the Website!")

def import_marketcap(url, market_cap_mapping, market_cap_workbook_path, market_cap_sheet_name):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("tbody")
        rows = table.find_all("tr")    
        if not os.path.exists(market_cap_workbook_path):
            workbook = Workbook()
        else:
            workbook = load_workbook(market_cap_workbook_path)
        if market_cap_sheet_name not in workbook.sheetnames:
            workbook.create_sheet(market_cap_sheet_name)
        sheet = workbook[market_cap_sheet_name]
        for row in rows:
            cells = row.find_all("td")
            metric = cells[0].get_text(strip=True)
            if metric in market_cap_mapping:
                row_num = market_cap_mapping[metric]
                values = [cell.get_text(strip=True) for cell in cells[1:21]] 
                for i, value in enumerate(values):
                    cell = sheet.cell(row=row_num, column=i+2)
                    cell.value = value
                    cell.alignment = Alignment(horizontal='right') 
        workbook.save(market_cap_workbook_path)
        print("Stock History Sheet Data from 'stockanalysis.com' Added to Excel File Successfully!")
    else:
        print("Failed to Fetch Data from the Website!")

print("\nG R E E N B A C K   A S S E T   M A N A G E M E N T , L L C .  |   S O F T W A R E   |")
ticker = input("\nENTER TICKER: ").lower()
print()
print("Accessing 'https://stockanalysis.com/' for Raw Data...")
income_url = f"https://stockanalysis.com/stocks/{ticker}/financials/?p=quarterly"
balance_url = f"https://stockanalysis.com/stocks/{ticker}/financials/balance-sheet/?p=quarterly"
cash_flow_url = f"https://stockanalysis.com/stocks/{ticker}/financials/cash-flow-statement/?p=quarterly"
market_cap_url = f"https://stockanalysis.com/stocks/{ticker}/financials/ratios/?p=quarterly"

import_income(income_url, income_mapping, income_workbook_path, income_sheet_name)
import_balance(balance_url, balance_mapping, balance_workbook_path, balance_sheet_name)
import_cash_flow(cash_flow_url, cash_flow_mapping, cash_flow_workbook_path, cash_flow_sheet_name)
import_marketcap(market_cap_url, market_cap_mapping, market_cap_workbook_path, market_cap_sheet_name)
os.startfile(market_cap_workbook_path)



