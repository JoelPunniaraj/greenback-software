# Datasprint, Inc. | GreenBack Asset Management Software

Portfolio Management & Financial Data Analysis Tool Features:
  - Actively Be Able To Track Your Portfolio
  - Be Able to Import Financial Documents via Python 
    to Excel for Data Analysis & Projection Models
  - Use Built-In Discounted Cash Flow Models

Past 5 Years of Data Imported from (stockanalysis.com)
  - Income Sheet Statement (Quarterly)
  - Balance Sheet Statement (Quarterly)
  - Cash Flow Sheet Statement (Quarterly)
  - Historical Market Capitalization (Quarterly)

Starting the Software:

```
$ cd greenback
$ run app.bat
```

Using Projections Feature (Ex. META):

```
$ D A T A S P R I N T ,  I N C .

$ Enter Option:      
$ - Projections      
$ - Valuations       
$ - Portfolio        

$ Enter Your Choice: projections

$ Projection Option 
$ 2y Model
$ 5y Model

$ Enter Option: 5y  

$ Ticker: meta

$ Accessing 'https://stockanalysis.com/' for Raw Data...
$ Income Sheet Data from 'stockanalysis.com' Added!
$ Balance Sheet Data from 'stockanalysis.com' Added!
$ Cash Flow Sheet Data from 'stockanalysis.com' Added!
$ Stock History Sheet Data from 'stockanalysis.com' Added!
```

An Excel Spreadsheet Will Open with the Following Sheets:
- income-sheet
- balance-sheet
- cash-flow-sheet
- stock-history
- condense-sheet
- projections



The 'income-sheet', 'balance-sheet', 'cash-flow-sheet', and 'stock-history'
has the Past 5 Years of Financial Data Imported and Organized Appropriately. 

The 'condense-sheet' Selects Necessary Metrics for the 'projections' Sheet and
Makes Sure the Data is Properly Formatted for Use. 

The 'projections' Sheet Houses all the Calculations and Charts to Show the 
Projections of the Selected Ticker

Projection Model for $META (Meta Platforms Inc)

![alt text](targets/meta.PNG)

You Can Also Extract Data For Each Metric From 'condense-sheets' . 'regression.py' 
Calculates the Projected Value for the Next Quarter

```
$ Available Metrics: 
$
$ Revenue
$ Cost of Revenue
$ Gross Profit
$ Operating Expenses
$ Operating Income
$ Income Tax
$ Net Income
$ Shares Outstanding (Basic) 
$ Shares Change
$ EPS (Basic)
$ Free Cash Flow
$ Free Cash Flow Per Share   
$ Dividend Per Share
$ Gross Margin
$ Operating Margin
$ Profit Margin
$ Free Cash Flow Margin      
$ Effective Tax Rate
$ EBITDA
$ EBITDA Margin
$ Cash & Equivalents
$ Total Current Assets       
$ Total Long-Term Assets     
$ Total Assets
$ Deferred Revenue
$ Total Current Liabilities  
$ Total Long-Term Liabilities
$ Total Liabilities
$ Total Debt
$ Retained Earnings
$ Shareholders' Equity       
$ Net Cash / Debt
$ Net Cash Per Share
$ Working Capital
$ Book Value Per Share       
$
$ Enter Metric: Free Cash Flow
$ 
$ [11812]
$ [13906]
$ [11175]
$ [7175] 
$ [5523] 
$ [337]  
$ [4668] 
$ [8761] 
$ [12735]
$ [9776] 
$ [8635] 
$ [7970] 
$ [9427] 
$ [6140] 
$ [622]
$ [7443]
$ [4983]
$ [5775]
$ [4983]
$ [5471]
$ 
$ Projected Value: [10206]
$ 
$ Enter Metric:
```

The Portfolio Option Allows You to Add Positions and Track Prices
- Live Prices from Yahoo Finance
- View Portfolio Statistics

```
$ D A T A S P R I N T ,  I N C .

$ Enter Option:      
$ - Projections      
$ - Valuations       
$ - Portfolio        

$ Enter Your Choice: portfolio

$ Options:
$ - 'Add' 
$ - 'View' 
$ - 'Edit' 
$ - 'Remove'         
$ -  Exit

$ Enter your choice: view
$ Do you want to sort the table first? (yes/no): yes
$ Sort Options:
$ - Sort by Value
$ - Sort by Profit        
$ - Exit

$ Enter your sort choice: value
$ +--------+--------+------------+--------------------+---------------+----------------+-------------+----------+
$ | Ticker | Shares | Cost Basis | Initial Investment | Current Price | Position Value | Profit/Loss | % Change |
$ +--------+--------+------------+--------------------+---------------+----------------+-------------+----------+
$ | META   |    175 |    $218.58 |         $38,251.50 |       $522.91 |     $91,509.25 |  $53,257.75 |  139.23% |
$ +--------+--------+------------+--------------------+---------------+----------------+-------------+----------+
$
$ Total Value: $91,509.25
$
$ Total Profit: $53,257.75
$
$ Options:
$ - Add 
$ - View 
$ - Edit 
$ - Remove 
$ - Exit
$
$ Enter your choice:  
```  

New Updates Coming in May 2024!
  - Will Be Able to Use Model for IPOs (Less Than 5 Years of Financial Data)
  - Will Be Able to Use Data from FRED.gov for Macroeconomic Analysis 
  - PyTorch Libraries Used to Generate More Accurate Projections
    using Equity Data, Macroeconomic Data, and Financial Documents
  - Automatic Portfolio Allocation Algorithm to Help Investors
    Manage and Adjust Positions Each Financial Quarter

Exciting Features in Development Coming Soon!

Written and Developed by Joel Punniaraj
Founder @ Datasprint, Inc.