import json
from datetime import datetime
import schedule
import time

DATA_FILE = "data.json"

def clear_today_orders():
    today = datetime.now().strftime('%Y-%m-%d')
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    except:
        data = {}

    if today in data:
        del data[today]
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"🗑 Cleared orders for {today}")
    else:
        print(f"ℹ️ No orders to clear for {today}")

# 🔁 Schedule for 12:00 PM daily
schedule.every().day.at("12:00").do(clear_today_orders)

if __name__ == "__main__":
    print("📅 Waiting to auto-clear curry orders every day at 12:00 PM...")
    while True:
        schedule.run_pending()
        time.sleep(1)
