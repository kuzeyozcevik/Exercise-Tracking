import requests
import datetime
import os

#sheety https://dashboard.sheety.co/projects/6933237ae0fa9a0546f38451
#text to nutrition https://app.100daysofpython.dev/services/nutrition
APP_ID = os.environ["NT_APP_ID"]

API_KEY =  os.environ["NT_API_KEY"]

url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheet_url = os.environ["SHEET_ENDPOINT"]

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}
auth_header = (os.environ["USERNAME"],os.environ["PASSWORD"])


data = {
    "query": input("What exercise did you do :"),
    "gender": "male",
    "weight_kg": 78,
    "height_cm": 175,
    "age": 16
}


response = requests.post(url, headers=headers, json=data)
result = response.json()
print(result["exercises"])

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "sayfa1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_url, json=sheet_inputs,auth=auth_header)
    print(sheet_response.text)
