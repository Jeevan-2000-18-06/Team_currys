import smtplib
import schedule
import time
import json
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import COMMASPACE

# Email config
EMAIL = "surabhijeevansai@gmail.com"
PASSWORD = "naas jtks weka kmlq"
TEAM_EMAILS = [
     "jeevan.s@stylosoftllp.com",
    "surabhijeevansai@gmail.com",
    "bhanu.b@styloworld.io",
    "neha.r@styloworld.io",
    "Nagaraju.k@styloworld.io",
    "charan.g@styloworld.io",
    "nikhilteja.ch@styloworld.io",
    "bharathkumar.p@styloworld.io",
    "naveen.ch@stangroupco.com",
    "murali.k@styloworld.io",
    "satyasai.k@styloworld.io",
    "saikeerthana@stylosoftllp.com",
    "nagireddy.g@styloworld.io",
    "priyanka.b@styloworld.io"
]

DATA_FILE = "data.json"

def send_curry_summary():
    date = datetime.now().strftime('%Y-%m-%d')
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            today_orders = data.get(date, {})
            if not today_orders:
                print("No curry orders today.")
                return
    except Exception as e:
        print("Could not load curry data.", e)
        return

    # Email body
    message = MIMEMultipart("alternative")
    message["Subject"] = "🍛 Curry Orders for Today"
    message["From"] = EMAIL
    message["To"] = COMMASPACE.join(TEAM_EMAILS)

    html = "<h3>Today's Curry Orders 🍛</h3><ul>"
    for name, info in today_orders.items():
        if isinstance(info, dict) and info.get("role") != "taker":
            curry = info.get("curry", "Unknown")
            paid = "✅" if info.get("paid") else "❌"
            html += f"<li><b>{name}</b>: {curry} – {paid}</li>"
    html += "</ul>"

    message.attach(MIMEText(html, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, TEAM_EMAILS, message.as_string())
        print("✅ Email sent successfully.")
    except Exception as e:
        print("❌ Error sending email:", e)

# Run daily at 12:12 PM
schedule.every().day.at("12:12").do(send_curry_summary)

if __name__ == "__main__":
    print("📧 Auto mail scheduler running... Waiting for 12:12 PM daily trigger.")
    while True:
        schedule.run_pending()
        time.sleep(1)
