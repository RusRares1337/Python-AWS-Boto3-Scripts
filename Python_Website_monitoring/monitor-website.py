import requests

response = requests.get('http://13.38.29.19:8080/')
if response.status_code == 200:
    print("Application is running successfully")
else:
    print('Application Down. Fix it!')