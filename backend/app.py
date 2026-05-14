from fastapi import FastAPI, HTTPException

from data.surf_spots import spots
from services.ranking import rank_spots
from services.ranking import rank_spot_over_time
from services.marine_api import (get_forecast, build_hourly_forecasts)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Surf Forecast API Running"}

@app.get("/forecast")
def forecast():

    try:
        forecast_data = get_forecast(
            latitude=54.5618,
            longitude=-8.2089
        )

        return forecast_data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/rankings")
def rankings():

    try:

        results = []

        for spot in spots:

            raw_forecast = get_forecast(
                latitude=spot["latitude"],
                longitude=spot["longitude"]
            )

            hourly_forecasts = build_hourly_forecasts(
                raw_forecast,
                hours=12
            )

            ranked = rank_spot_over_time(
                hourly_forecasts,
                spot
            )

            results.append(ranked)

        results.sort(
            key=lambda x: x["best_score"],
            reverse=True
        )

        return {
            "rankings": results
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )