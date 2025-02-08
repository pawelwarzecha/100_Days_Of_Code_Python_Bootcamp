import requests
from datetime import datetime
import smtplib

MY_LAT = 52.229675 # Your latitude
MY_LONG = 21.012230 # Your longitude

def is_iss_close():
    if MY_LAT -5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    else:
        return False

def is_it_nighttime():
    if time_now.hour < sunrise or time_now.hour > sunset:
        return True
    else:
        return False

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

if is_iss_close() == True and is_it_nighttime() == True:
    my_email = "email@email.com"  # email address
    password = "password"  # app code from email account

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
                    from_addr=my_email,
                    to_addrs=my_email,
                    msg=f"Subject:ISS is overhead\n\nInternational Space Station is overhead! Look up!")


