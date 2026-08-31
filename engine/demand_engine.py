def calculate_demand(product, market_score):
    if "Pouch" in product:
        return min(100, market_score + 5)
    return min(100, market_score)