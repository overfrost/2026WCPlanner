import streamlit as st
import pandas as pd
from streamlit_calendar import calendar

st.set_page_config(page_title="2026 World Cup Planner", layout="wide")

# --- DATA LOADING ---
@st.cache_data
def load_data():
    df = pd.read_csv('data/matches.csv')
    
    # Map groups to specific colors for a better UI
    group_colors = {
        "A": "#006341", "B": "#DA291C", "C": "#003580", "D": "#FFCD00",
        "E": "#000000", "F": "#F1C40F", "G": "#2E86C1", "H": "#8E44AD"
    }
    
    calendar_events = []
    for _, row in df.iterrows():
        calendar_events.append({
            "title": f"{row['Teams']} ({row['Host_City']})",
            "start": row['Date'],
            "backgroundColor": group_colors.get(row['Group'], "#3D9DF3"),
            "extendedProps": {
                "venue": row['Venue'],
                "kickoff": row['Kickoff_Time_ET'],
                "group": row['Group']
            }
        })
    return calendar_events

events = load_data()

# --- UI SETUP ---
st.title("⚽ 2026 World Cup Schedule & Analysis")

# Sidebar for filters
st.sidebar.header("Filters")
selected_groups = st.sidebar.multiselect(
    "Select Groups", 
    options=["A", "B", "C", "D", "E", "F", "G", "H"],
    default=["A", "B", "C", "D"]
)

# Filter events based on sidebar selection
filtered_events = [e for e in events if e['extendedProps']['group'] in selected_groups]

# Layout columns
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Match Calendar")
    calendar_options = {
        "initialView": "dayGridMonth",
        "initialDate": "2026-06-11",
        "headerToolbar": {
            "left": "prev,next today",
            "center": "title",
            "right": "dayGridMonth,listWeek"
        }
    }
    
    # Render the calendar and capture user interaction
    state = calendar(events=filtered_events, options=calendar_options)

with col2:
    st.subheader("Match Details")
    
    # Logic to show details when a match is clicked
    if state.get("callback") == "eventClick":
        event_data = state["eventClick"]["event"]
        props = event_data["extendedProps"]
        
        st.success(f"### {event_data['title']}")
        st.write(f"**Stadium:** {props['venue']}")
        st.write(f"**Kickoff:** {props['kickoff']} (ET)")
        st.write(f"**Group:** {props['group']}")
        
        # Space for your future analysis
        st.button("Run Head-to-Head Analysis")
    else:
        st.info("Click a match on the calendar to see details here.")
    
    st.divider()
    st.metric(label="Total Matches in View", value=len(filtered_events))