import requests
import smtplib
import os

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

response = requests.get('http://13.38.29.19:8080/')
if response.status_code == 200:
    print("Application is running successfully")
else:
    print('Application Down. Fix it!')
    # send email to me
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        msg = EMAIL_ADDRESS, EMAIL_PASSWORD, "Subject: SITE DOWN\nFix the issue! Rstart the application."
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, msg)

