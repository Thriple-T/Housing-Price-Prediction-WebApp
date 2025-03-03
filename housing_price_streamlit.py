import streamlit as st
import pickle
import numpy as np

# Streamlit UI
st.title("Housing Price Prediction App")
st.write("Please Enter the details to predict the price of the house.")

# Input fields

LotArea =st.number_input("Lot Area", min_value=1300, max_value=215245, value=10000 )
OverallQual = st.number_input("Overall Quality", min_value=1, max_value=10, value=5)
OverallCond = st.number_input("Overall Condition", min_value=1, max_value=10, value=5)
YearBuilt = st.number_input("Year Built", min_value=1872, max_value=2010, value=2000)
YearRemodAdd = st.number_input("Year Remodelled", min_value=1950, max_value=2010, value=2000)
TotalBsmtSF = st.number_input("Total Basement Area", min_value=0, max_value=6110, value=1000)
firstfloor = st.number_input("First Floor Area", min_value=334, max_value=4692, value=1000)
secondfloor = st.number_input("Second Floor Area", min_value=0, max_value=2065, value=1000)
GrlivArea = st.number_input("Ground Living Area", min_value=334, max_value=5642, value=1000)
BsmtFullBath = st.number_input("Basement Full Bathrooms", min_value=0, max_value=3, value=1)
BsmtHalfBath = st.number_input("Basement Half Bathrooms", min_value=0, max_value=2, value=1)
FullBath = st.number_input("Full Bathrooms", min_value=0, max_value=3, value=1)
HalfBath = st.number_input("Half Bathrooms", min_value=0, max_value=2, value=1)
BedroomAbvGr = st.number_input("Bedrooms", min_value=0, max_value=8, value=3)
KitchenAbvGr = st.number_input("Kitchens", min_value=0, max_value=3, value=1)
TotRmsAbvGrd = st.number_input("Total Rooms", min_value=2, max_value=14, value=6)
Fireplaces = st.number_input("Fireplaces", min_value=0, max_value=3, value=1)
GarageCars = st.number_input("Garage Cars", min_value=0, max_value=4, value=2)
GarageArea = st.number_input("Garage Area", min_value=0, max_value=1418, value=500)
WoodDeckSF = st.number_input("Wood Deck Area", min_value=0, max_value=857, value=200)
OpenPorchSF = st.number_input("Open Porch Area", min_value=0, max_value=547, value=100)
EnclosedPorch = st.number_input("Enclosed Porch Area", min_value=0, max_value=552, value=100)
SsnPorch = st.number_input("3 Season Porch Area", min_value=0, max_value=508, value=100)
ScreenPorch = st.number_input("Screen Porch Area", min_value=0, max_value=480, value=100)
PoolArea = st.number_input("Pool Area", min_value=0, max_value=738, value=100)
MiscVal = st.number_input("Miscellaneous Value", min_value=0, max_value=15500, value=100)
MoSold = st.number_input("Month Sold", min_value=1, max_value=12, value=6)
YrSold = st.number_input("Year Sold", min_value=2006, max_value=2010, value=2008)

with open("house_pricing_model.pkl", 'rb') as f:
    loaded_model=pickle.load(f)
  
if st.button("Predict"):
    try:
        input_features=np.array([[LotArea, OverallQual, OverallCond, YearBuilt, YearRemodAdd, TotalBsmtSF, firstfloor, secondfloor, GrlivArea, BsmtFullBath, BsmtHalfBath, FullBath, HalfBath, BedroomAbvGr, KitchenAbvGr, TotRmsAbvGrd, Fireplaces, GarageCars, GarageArea, WoodDeckSF, OpenPorchSF, EnclosedPorch, SsnPorch, ScreenPorch, PoolArea, MiscVal, MoSold, YrSold]])
        value=loaded_model.predict(input_features)
        st.write(f"The price of the house is: ${value[0]:.2f}")
    except Exception as e:
        st.error(f"Error: {e}")
