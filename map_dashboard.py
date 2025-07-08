# map_dashboard.py
import streamlit as st
import folium
from pymongo import MongoClient
from geopy.geocoders import Nominatim
from streamlit_folium import st_folium

# Setup
st.set_page_config(page_title="Disaster Misinformation Tracker", layout="wide")
st.title("🌍 Real-Time Reddit Disaster Posts")

client = MongoClient("mongodb://localhost:27017/")
collection = client["rumor_db"]["reddit_posts"]
geolocator = Nominatim(user_agent="geoapi")

# Fetch only processed + labeled posts
posts = collection.find({"processed": True, "location": {"$ne": []}})

m = folium.Map(location=[20, 0], zoom_start=2)

for post in posts:
    for loc in post["location"]:
        try:
            geo = geolocator.geocode(loc)
            if geo:
                folium.Marker(
                    [geo.latitude, geo.longitude],
                    popup=f"<b>{post['title'][:100]}</b><br>Label: {post['label']}<br>Confidence: {post['confidence']}"
                ).add_to(m)
        except:
            continue

st_folium(m, width=1200, height=600)
