import os
import smtplib
import random
import logging
from datetime import datetime
import pandas as pd
from email.utils import formataddr
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")


def get_smtp_server(email):
    domain = email.split("@")[1]
    if domain == "gmail.com":
        return "smtp.gmail.com"
    elif domain == "yahoo.com":
        return "smtp.mail.yahoo.com"
    elif domain == "outlook.com":
        return "smtp.office365.com"
    else:
        raise ValueError("Unsupported email provider.")


def get_today_tuple():
    today = datetime.now()
    return (today.month, today.day)


def load_birthdays(file_path="birthdays.csv"):
    data = pd.read_csv(file_path)
    return {(row["month"], row["day"]): row for (_, row) in data.iterrows()}


def personalize_letter(name, template_path):
    try:
        with open(template_path) as file:
            content = file.read()
            return content.replace("[NAME]", name)
    except FileNotFoundError:
        logging.error(f"Template {template_path} not found.")
        return None


def send_email(to_email, subject, message):
    smtp_address = get_smtp_server(MY_EMAIL)
    try:
        with smtplib.SMTP(smtp_address, 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=formataddr(("Birthday Bot", MY_EMAIL)),
                to_addrs=to_email,
                msg=f"Subject:{subject}\n\n{message}",
            )
        logging.info(f"Email sent to {to_email}")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")


def main():
    today = get_today_tuple()
    birthdays = load_birthdays()

    if today in birthdays:
        person = birthdays[today]
        template_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        message = personalize_letter(person["name"], template_path)

        if message:
            send_email(person["email"], "Happy Birthday!", message)
        else:
            logging.warning("Could not prepare birthday message.")
    else:
        logging.info("No birthdays today.")


if __name__ == "__main__":
    main()
