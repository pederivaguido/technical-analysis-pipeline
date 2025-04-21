import yfinance as yf
import os
import json
import pandas as pd
from datetime import datetime
from pathlib import Path

# ========== SETTINGS ==========
TICKERS = ["SQ", "PYPL", "FISV", "ADYEN.AS", "MELI", "NU", "SOFI", "UPST", "V", "MA"]
PRICE_DIR = Path("data_ingestion/output/prices")
FUND_DIR = Path("data_ingestion/output/fundamentals")
TODAY = datetime.now().strftime("%Y-%m-%d")

# Ensure output directories exist
PRICE_DIR.mkdir(parents=True, exist_ok=True)
FUND_DIR.mkdir(parents=True, exist_ok=True)

def fetch_and_append_price(symbol):
    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period="10d")  # Buffer of 5 days in case of holidays, weekends, API flakiness, etc.
        if hist.empty:
            print(f"⚠️ No data for {symbol}")
            return

        hist.reset_index(inplace=True)
        hist["Date"] = hist["Date"].dt.strftime("%Y-%m-%d")

        csv_path = PRICE_DIR / f"{symbol}.csv"

        if csv_path.exists():
            existing = pd.read_csv(csv_path)

            # ✅ Ensure both Date columns are strings
            hist["Date"] = hist["Date"].astype(str)
            existing["Date"] = existing["Date"].astype(str)

            new_rows = hist[~hist["Date"].isin(existing["Date"])]
            if not new_rows.empty:
                updated = pd.concat([existing, new_rows]).sort_values("Date")
                updated.to_csv(csv_path, index=False)
                print(f"📈 Updated {symbol}.csv with {len(new_rows)} new rows")
            else:
                print(f"⏩ {symbol}.csv already up to date")
        else:
            hist.to_csv(csv_path, index=False)
            print(f"✅ Created {symbol}.csv with full history")

    except Exception as e:
        print(f"❌ Error fetching prices for {symbol}: {e}")

def fetch_and_store_fundamentals(symbol):
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        if not info:
            print(f"⚠️ No fundamentals for {symbol}")
            return
        snapshot_path = FUND_DIR / f"{symbol}_{TODAY}.json"
        with open(snapshot_path, "w") as f:
            json.dump(info, f, indent=2)
        print(f"🧠 Stored fundamentals snapshot for {symbol}")
    except Exception as e:
        print(f"❌ Error fetching fundamentals for {symbol}: {e}")

# ========== MAIN LOOP ==========

for ticker in TICKERS:
    print(f"\n🔄 Processing {ticker}")
    fetch_and_append_price(ticker)
    fetch_and_store_fundamentals(ticker)