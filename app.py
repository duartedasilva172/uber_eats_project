import streamlit as st
import pandas as pd 
import numpy as np 
from datetime import datetime, timedelta
import os

st.title("Courier Tracker")
st.subheader("Welcome to you personal courier tracker tool")

st.image("courier.png", width= 400)

st.markdown("""
This free tool is designed to help couriers track their:
* Sessions (time, earnings, efficiency)
* Individual Trips (distance, tips, zones) 
* Expensees (coming soon!)
* Performance metrics

Use the buttons below to get started!          
""")

# Navigation buttons 
col1, col2 = st.columns(2)

with col1: 
    if st.button("Go to Session Entry"):
        st.switch_page("pages/sessions_entry.py")

with col2: 
    if st.button("Go to Trip Entry"):
        st.switch_page("pages/trips_entry.py")