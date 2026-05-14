def degree_to_compass(deg):
    if deg is None:
        return None
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                  "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    idx = int((deg / 22.5) + 0.5) % 16
    return directions[idx]