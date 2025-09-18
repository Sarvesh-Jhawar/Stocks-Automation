# Daily Stock Update Automation

This repository contains an automated script that fetches and tracks the latest stock data for a predefined list of companies. The project is designed to run daily, generating updated data and visualization plots, and committing them back to the repository.

### Features

* **Daily Stock Data Fetching**: Automatically fetches today's stock data for a list of companies.
* **Data Storage**: Appends the fetched data to a `stock_data.csv` file, maintaining a historical record.
* **Plot Generation**: Creates and saves one-month trend plots for each tracked stock, saved as PNG images.
* **Automated Workflow**: Utilizes a GitHub Actions workflow to run the script automatically every day at 12:00 UTC.

### Tracked Stocks
The automation script currently tracks the following stocks:
* **Large Cap**: `RELIANCE.NS`, `TCS.NS`, `INFY.NS`, `SBIN.NS`, `AXISBANK.NS`, `KOTAKBANK.NS`
* **Mid Cap**: `HINDZINC.NS`, `SOLARINDS.NS`, `MAZDOCK.NS`, `HDFCAMC.NS`, `MAXHEALTH.NS`, `CUMMINSIND.NS`
* **Small Cap**: `OSWALPUMPS.NS`, `SWARAJENG.NS`, `LAURUSLABS.NS`, `KAYNES.NS`, `DENTALKART.NS`, `GCSL.NS`

### How It Works

The core of the project is the `fetch_stocks.py` Python script, which uses the `yfinance`, `pandas`, and `matplotlib` libraries to perform the following steps:
1.  **Fetch Data**: Uses the `yfinance` library to get the latest close price and one-month historical data for each stock listed in the script.
2.  **Calculate Change**: Calculates the percentage change between the opening and closing prices for the day.
3.  **Save to CSV**: Appends the stock, date, open price, close price, and percentage change to a CSV file located at `data/stock_data.csv`.
4.  **Generate Plots**: Creates a line plot of the last month's trend for each stock and saves it as a PNG file in the `data/plots` directory.

The entire process is automated by a GitHub Actions workflow defined in the `.github/workflows/daily_update.yml` file. This workflow is configured to:
* Checkout the repository.
* Set up a Python 3.10 environment.
* Install the required dependencies (`yfinance`, `pandas`, `matplotlib`).
* Execute the `fetch_stocks.py` script.
* Commit the updated CSV and plot files back to the repository with a timestamped commit message.

### Outputs

The automation generates two types of files:
* `data/stock_data.csv`: A CSV file containing the daily open and close prices and the percentage change for each stock.
* `data/plots/`: A directory containing PNG plots showing the 1-month trend for each tracked stock.
