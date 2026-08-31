def calculate_market_score(row):
    score = (
        row.smoker*0.30 +
        row.income*0.25 +
        row.tourism*0.25 +
        row.retail*0.20
    )
    return round(score)