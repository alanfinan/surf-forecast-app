
from backend.logic.scoring import score_spot

def rank_spots(forecast, spots):
    results = []

    for spot in spots:
        scored = score_spot(forecast, spot)
        results.append(scored)

    results.sort(key=lambda x: x["score"], reverse=True)
    return results