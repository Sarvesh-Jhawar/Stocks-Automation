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
current_time = datetime.now().strftime("%H:%M:%S")
current_date = datetime.now().strftime("%Y-%m-%d")

for stock in STOCKS:
    ticker = yf.Ticker(stock)
    data = ticker.history(period="1d")
    if not data.empty:
        close_price = data["Close"].iloc[-1]
        open_price = data["Open"].iloc[-1]
        change_percent = ((close_price - open_price) / open_price) * 100

        new_data_list.append({
            "Stock": stock,
            "Date": current_date,
            "Time": current_time,
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
        plt.savefig(f"data/plots/{stock}_{current_date}.png")
        plt.close()

# -------------------------------
# Save CSV (append new data)
# -------------------------------
if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
else:
    df = pd.DataFrame(columns=["Stock", "Date", "Time", "Open", "Close", "Change (%)"])

new_df = pd.DataFrame(new_data_list)
final_df = pd.concat([df, new_df], ignore_index=True)

final_df.to_csv(csv_file, index=False)

print("✅ Stock data updated successfully!")
