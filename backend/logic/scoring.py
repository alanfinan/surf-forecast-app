from utils.directions import degree_to_compass

def normalize_direction(direction):
    if direction is None:
        return None
    if isinstance(direction, (int, float)):
        return degree_to_compass(direction)
    return str(direction).upper().strip()

def score_direction(actual, ideal_list, points=30):
    actual = normalize_direction(actual)
    ideal_list = [normalize_direction(d) for d in ideal_list]

    if actual in ideal_list:
        return points
    return 0

def score_period(period, minimum_period):
    if period is None:
        return 0
    return 20 if period >= minimum_period else 0

def score_height(height, min_height, max_height):
    if height is None:
        return 0
    if min_height <= height <= max_height:
        return 20
    return 0

def score_tide(tide_label, ideal_tide):
    if not tide_label or not ideal_tide:
        return 0

    tide_label = str(tide_label).lower().strip()
    ideal_tide = str(ideal_tide).lower().strip()

    if ideal_tide == "all":
        return 15

    if tide_label == ideal_tide:
        return 15

    if ideal_tide == "low-mid" and tide_label in ["low", "mid", "low-mid"]:
        return 15

    return 0

def score_spot(forecast, spot):

    swell_score = score_direction(
        forecast.get("wave_direction"),
        spot.get("ideal_swell_directions", []),
        points=30
    )

    wind_score = score_direction(
        forecast.get("wind_direction"),
        spot.get("ideal_wind_directions", []),
        points=30
    )

    period_score = score_period(
        forecast.get("wave_period"),
        spot.get("minimum_period", 0)
    )

    height_score = score_height(
        forecast.get("wave_height"),
        spot.get("ideal_wave_height_min", 0),
        spot.get("ideal_wave_height_max", 999)
    )

    tide_score = score_tide(
        forecast.get("tide"),
        spot.get("ideal_tide")
    )

    wind_speed_score = score_wind_speed(
    forecast.get("wind_speed"),
    spot.get("ideal_wind_speed_max", 15)
)

    total_score = (
        swell_score
        + wind_score
        + period_score
        + height_score
        + tide_score
        + wind_speed_score
    )

    return {
        "spot": spot["name"],
        "score": total_score,

        "breakdown": {
            "swell_direction": swell_score,
            "wind_direction": wind_score,
            "wave_period": period_score,
            "wave_height": height_score,
            "tide": tide_score,
            "wind_speed": wind_speed_score
        }
    }

def score_wind_speed(speed, max_ideal_speed):

    if speed is None:
        return 0

    if speed <= 5:
        return 20

    elif speed <= max_ideal_speed:
        return 15

    elif speed <= max_ideal_speed + 5:
        return 5

    return 0