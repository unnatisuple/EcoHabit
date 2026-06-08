import streamlit as st
import pandas as pd
from ui import apply_background
apply_background()

st.set_page_config(page_title="EcoHabit🌱", layout="wide")

st.title("🌎 Carbon Footprint Calculator")

electricity = st.number_input("Monthly electricity (kWh)",50,1000)
car_km = st.number_input("Car travel per week (km)",0,500)
flights = st.number_input("Flights per year",0,20)
meat_meals = st.number_input("Meat meals per week",0,21)

co2_electricity = electricity * 0.85
co2_car = car_km * 0.21 * 4
co2_flight = flights * 90
co2_meat = meat_meals * 2.5 * 4

total = co2_electricity + co2_car + co2_flight + co2_meat

st.metric("Monthly CO₂ Emission",round(total,2))

trees = total / 21

st.metric("Trees Needed to Offset",int(trees))
st.info("Planting these many trees annually can offset your emissions.")

chart = pd.DataFrame({
"Source":["Electricity","Transport","Flights","Diet"],
"CO2":[co2_electricity,co2_car,co2_flight,co2_meat]
})


st.bar_chart(chart.set_index("Source"))
st.info("The taller the bar, the more CO₂ that activity produces.")

# import streamlit as st
# import pandas as pd

# st.title("📊 Eco Analytics")

# data = pd.DataFrame({
# "Month":["Jan","Feb","Mar","Apr","May"],
# "Tokens":[10,30,50,80,120]
# })

# st.line_chart(data.set_index("Month"))