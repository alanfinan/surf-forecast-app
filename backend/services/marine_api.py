import requests

def get_marine_forecast(latitude, longitude):

    url = "https://marine-api.open-meteo.com/v1/marine"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "wave_height,wave_direction,wave_period"
    }

    response = requests.get(url, params=params)

    data = response.json()

    return {
        "wave_height": data["hourly"]["wave_height"][0],
        "wave_direction": data["hourly"]["wave_direction"][0],
        "wave_period": data["hourly"]["wave_period"][0]
    }