import smtplib
from random import randint
import pandas
import datetime as dt

GMAIL = "smtp.gmail.com"
YAHOO = "smtp.mail.yahoo.com"
HOTMAIL = "smtp.live.com"
OUTLOOK = "smtp-mail.outlook.com"

my_email = "email@email.com" #email address
password = "password" #app code from email account

current_time = dt.datetime.now()
today_month = current_time.month
today_day = current_time.day

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if (today_month, today_day) in birthdays_dict:
    birthday_row = birthdays_dict[today_month, today_day]
    with open(f"letter_templates/letter_{randint(1,3)}.txt") as text:
        letter_body = text.read()
        letter_body = letter_body.replace("[NAME]", birthday_row["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
                    from_addr=my_email,
                    to_addrs=birthday_row["email"],
                    msg=f"Subject:Happy Birthday!\n\n{letter_body}")