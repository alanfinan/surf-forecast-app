from logic.scoring import score_spot

def rank_spots(forecast, spots):
    results = []

    for spot in spots:
        scored = score_spot(forecast, spot)
        results.append(scored)

    results.sort(key=lambda x: x["score"], reverse=True)
    return results

def rank_spot_over_time(forecasts, spot):

    scored_forecasts = []

    for forecast in forecasts:

        scored = score_spot(forecast, spot)

        scored_forecasts.append({
            "time": forecast["time"],
            "score": scored["score"],
            "breakdown": scored["breakdown"]
        })

    scored_forecasts.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    best_window = scored_forecasts[0]

    return {
        "spot": spot["name"],
        "best_score": best_window["score"],
        "best_time": best_window["time"],
        "best_breakdown": best_window["breakdown"],
        "top_windows": scored_forecasts[:3]
    }