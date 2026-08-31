def sales_forecast(score, outlets, price):

    low_units = round(outlets*(score/100)*20)
    base_units = round(outlets*(score/100)*50)
    high_units = round(outlets*(score/100)*100)

    return {
        "low_units": low_units,
        "base_units": base_units,
        "high_units": high_units,
        "low_revenue": low_units*price,
        "base_revenue": base_units*price,
        "high_revenue": high_units*price
    }