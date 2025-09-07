import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# -------------------------------
# Configurable: List of stock tickers
# -------------------------------
STOCKS = ["AAPL", "TSLA", "MSFT", "RELIANCE.NS", "TCS.NS"]

# Ensure folders exist
os.makedirs("data/plots", exist_ok=True)

# File path for CSV
csv_file = "data/stock_data.csv"

# -------------------------------
# Fetch stock data
# -------------------------------
new_data_list = []
for stock in STOCKS:
    ticker = yf.Ticker(stock)
    data = ticker.history(period="1d")
    if not data.empty:
        close_price = data["Close"].iloc[-1]
        open_price = data["Open"].iloc[-1]
        change_percent = ((close_price - open_price) / open_price) * 100

        new_data_list.append({
            "Stock": stock,
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Open": round(open_price, 2),
            "Close": round(close_price, 2),
            "Change (%)": round(change_percent, 2)
        })

        # Save plot
        hist = ticker.history(period="1mo")
        plt.figure(figsize=(6, 4))
        plt.plot(hist.index, hist["Close"], label=f"{stock} Close Price")
        plt.title(f"{stock} - Last 1 Month Trend")
        plt.xlabel("Date")
        plt.ylabel("Price (USD/INR)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"data/plots/{stock}_{datetime.now().strftime('%Y-%m-%d')}.png")
        plt.close()

# -------------------------------
# Save CSV (append or update new data)
# -------------------------------
if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
else:
    df = pd.DataFrame(columns=["Stock", "Date", "Open", "Close", "Change (%)"])

new_df = pd.DataFrame(new_data_list)
current_date_str = datetime.now().strftime("%Y-%m-%d")

for index, row in new_df.iterrows():
    stock_ticker = row['Stock']
    existing_row_index = df[(df['Stock'] == stock_ticker) & (df['Date'] == current_date_str)].index
    if not existing_row_index.empty:
        # Update existing row
        df.loc[existing_row_index, 'Open'] = row['Open']
        df.loc[existing_row_index, 'Close'] = row['Close']
        df.loc[existing_row_index, 'Change (%)'] = row['Change (%)']
    else:
        # Append new row
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)

df.to_csv(csv_file, index=False)

print("✅ Stock data updated successfully!")