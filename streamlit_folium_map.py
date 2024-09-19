import streamlit as st
import pandas as pd
import folium 
from streamlit_folium import st_folium

df = pd.read_csv("https://github.com/ilpovirt/streamlit_map/blob/main/GPSdata.csv")

#Create a map where the center is at start_lat start_long and zoom level is defined
start_lat = df['Latitude (°)'].mean()
start_long = df['Longitude (°)'].mean()
map = folium.Map(location = [start_lat,start_long], zoom_start = 14)

#Draw the map
folium.PolyLine(df[['Latitude (°)','Longitude (°)']], color = 'blue', weight = 3.5, opacity = 1).add_to(map)

st.title('My journey to work')

#Define map dimensions and show the map
st_map = st_folium(map, width=900, height=650)
