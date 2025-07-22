import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import COMMASPACE, formataddr
import schedule
import time

# Email config
EMAIL = "surabhijeevansai@gmail.com"
SENDER_NAME = "Team Currys"
PASSWORD = "naas jtks weka kmlq"

TEAM_EMAILS = [
    "jeevan.s@stylosoftllp.com",
    "surabhijeevansai@gmail.com",
    "murali.k@styloworld.io",
    "bhanu.b@styloworld.io",
    "neha.r@styloworld.io",
    "Nagaraju.k@styloworld.io",
    "charan.g@styloworld.io",
    "nikhilteja.ch@styloworld.io",
    "bharathkumar.p@styloworld.io",
    "naveen.ch@stangroupco.com",
    "satyasai.k@styloworld.io",
    "saikeerthana@stylosoftllp.com",
    "nagireddy.g@styloworld.io",
    "priyanka.b@styloworld.io"
]

def send_reminder_email():
    subject = "🍛 Reminder: Submit Your Curry Order Today"

    html_body = """
    <div style="font-family: Arial, sans-serif; color: #333; padding: 20px; border: 1px solid #e0e0e0; border-radius: 10px;">
      <h2 style="color: #e76f51;">Hello Team 👋</h2>
      <p>This is a gentle reminder to <strong>submit your curry order</strong> for today's lunch 🍛.</p>
      <p style="margin: 20px 0;">
        <a href="https://team-currys-1.onrender.com"
           style="background-color: #2a9d8f; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: bold;">
          Submit Curry Order Now
        </a>
      </p>
      <p>If you have already submitted your order, please ignore this email.</p>
      <hr style="margin-top: 30px; border: none; border-top: 1px solid #ddd;" />
    
    </div>
    """

for recipient in TEAM_EMAILS:
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = formataddr((SENDER_NAME, EMAIL))
    message["To"] = recipient
    message.attach(MIMEText(html_body, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, recipient, message.as_string())
        print(f"✅ Email sent to {recipient}")
    except Exception as e:
        print(f"❌ Failed to send email to {recipient}: {e}")

# 🔁 Schedule daily at 12:12 PM
schedule.every().day.at("12:12").do(send_reminder_email)

if __name__ == "__main__":
    print("📧 Waiting to send daily curry reminder at 12:12 PM...")
    
    # 🔧 Uncomment this line to test instantly:
    # send_reminder_email()

    while True:
        schedule.run_pending()
        time.sleep(1)
