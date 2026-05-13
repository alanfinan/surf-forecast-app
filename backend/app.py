from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/forecast")
def forecast():

    url = "https://marine-api.open-meteo.com/v1/marine"

    params = {
        "latitude": 54.5618,
        "longitude": -8.2089,
        "hourly": "wave_height,wave_period,wave_direction"
    }

    response = requests.get(url, params=params)

    return response.json()