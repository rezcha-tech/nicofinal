import streamlit as st
import pandas as pd
import plotly.express as px

from engine.market_engine import calculate_market_score
from engine.demand_engine import calculate_demand
from engine.location_engine import recommend_location
from engine.forecast_engine import sales_forecast

st.set_page_config(page_title="NICO AI Research Platform V4", layout="wide")

st.title("NICO AI Research Platform V4")
st.subheader("Nicotine Pouch & Nicotine Gum Market Intelligence")

cities = pd.read_csv("database/cities.csv")
competitors = pd.read_csv("database/competitors.csv")

city = st.selectbox("Distribution City", cities["city"].tolist())
product = st.selectbox(
    "Product",
    ["Nicotine Pouch 8mg", "Nicotine Gum 4mg"]
)

price = st.number_input("Product Price (IDR)", value=62500, step=2500)
outlet = st.number_input("Target Outlet", value=50)

if st.button("GENERATE MARKET ANALYSIS"):

    market = cities[cities.city == city].iloc[0]

    score = calculate_market_score(market)
    demand = calculate_demand(product, score)

    locations = recommend_location(city)
    forecast = sales_forecast(score, outlet, price)

    col1,col2,col3 = st.columns(3)

    col1.metric("Market Opportunity", f"{score}/100")
    col2.metric("Demand Score", f"{demand}/100")
    col3.metric("Base Revenue", f"Rp {forecast['base_revenue']:,.0f}")

    st.header("City Intelligence")
    st.write({
        "City": city,
        "Purchasing Power": market.income,
        "Smoker Market": market.smoker,
        "Tourism Exposure": market.tourism,
        "Retail Fit": market.retail
    })

    st.header("Recommended Retail Area")
    st.write(locations)

    st.header("Sales Scenario")
    st.write(forecast)

    st.header("Competitor Intelligence")
    st.dataframe(competitors)

    chart = pd.DataFrame({
        "Scenario":["Conservative","Base","Optimistic"],
        "Revenue":[
            forecast["low_revenue"],
            forecast["base_revenue"],
            forecast["high_revenue"]
        ]
    })

    st.plotly_chart(
        px.bar(chart, x="Scenario", y="Revenue"),
        use_container_width=True
    )