import requests
from _datetime import datetime

APP_ID = "<<APP_ID>>"
API_KEY = "<<API_KEY>>"
GENDER = "female"
WEIGHT = 1
HEIGHT = 2
AGE = 3
QUERY = input("Tell me which exercise you did: ")
today = datetime.now()
USER = "<<USERNAME>>"
PASS = "<<PASSWORD>>"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/98b013e70fc6560bb992a4610bca2509/workoutTracking/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

user_params = {
    "query": QUERY,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

nutri_response = requests.post(url=nutritionix_endpoint, json=user_params, headers=headers)

date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

data = nutri_response.json()["exercises"]
for exercise in range(len(data)):
    sheety_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": data[exercise]["name"].title(),
            "duration": data[exercise]["duration_min"],
            "calories": data[exercise]["nf_calories"]
        }
    }
    sheety_response = requests.post(url=sheety_endpoint, json=sheety_params, auth=(USER, PASS))
