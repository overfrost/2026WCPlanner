import streamlit as st
import pandas as pd
from streamlit_calendar import calendar

st.set_page_config(page_title="2026 World Cup Planner", layout="wide")

st.title("⚽ 2026 World Cup Schedule & Analysis")

# Sidebar for filters
st.sidebar.header("Filters")
group_filter = st.sidebar.multiselect("Select Groups", ["A", "B", "C", "D", "E", "F", "G", "H"])

# Layout columns
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Match Calendar")
    # Basic calendar setup
    calendar_options = {
        "initialView": "dayGridMonth",
        "initialDate": "2026-06-11",
        "headerToolbar": {
            "left": "prev,next today",
            "center": "title",
            "right": "dayGridMonth,listWeek"
        }
    }
    
    # Placeholder match
    events = [
        {
            "title": "Opening Match: Mexico vs TBD",
            "start": "2026-06-11",
            "backgroundColor": "#006341"
        }
    ]
    
    calendar(events=events, options=calendar_options)

with col2:
    st.subheader("Analysis & Insights")
    st.info("Select a match on the calendar to see stadium details and historical head-to-head stats.")
    
    # Example metric for your analysis
    st.metric(label="Total Matches", value="104")
    st.metric(label="Host Cities", value="16")
