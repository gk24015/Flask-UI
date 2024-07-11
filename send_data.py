import requests
import json
def send_data(username,data):
    url=f"http://localhost:5000/{username}"
    headers={'Content-Type':'application/json'}
    response=requests.post(url,data=data,headers=headers)

data={"hey"}

send_data("ABC",data)