def calculate_surf_score(spot, forecast):

    score = 0

    if forecast["wave_height"] >= spot["minimum_wave_height"]:
        score += 40

    if forecast["wave_period"] >= spot["minimum_period"]:
        score += 40

    score += 20

    return score