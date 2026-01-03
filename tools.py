import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import (
    SMTP_SERVER,
    SMTP_PORT,
    SENDER_EMAIL,
    SENDER_APP_PASSWORD,
    EXCEL_OUTPUT_PATH,
)

# -------- TOOL 1: SEND EMAIL --------
def send_email_tool(recipient: str, subject: str, body: str) -> str:
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = recipient
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_APP_PASSWORD)
        server.send_message(msg)
        server.quit()

        return f"Email sent successfully to {recipient}"

    except Exception as e:
        return f"Failed to send email: {str(e)}"


# -------- TOOL 2: SAVE EXCEL --------
def save_excel_tool(rows: list) -> str:
    try:
        df = pd.DataFrame(rows)
        df.to_excel(EXCEL_OUTPUT_PATH, index=False)
        return f"Excel saved at {EXCEL_OUTPUT_PATH}"
    except Exception as e:
        return f"Failed to save Excel: {str(e)}"
