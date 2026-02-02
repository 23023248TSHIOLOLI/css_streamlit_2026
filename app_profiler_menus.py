

# Necessary imports
import streamlit as st
import pandas as pd
import numpy as np

# Set page title
# Set up Streamlit page
st.set_page_config(page_title="Researcher Profile and STEM Data Explorer", layout="wide")

# Sidebar Menu

# Dummy STEM data
physics_data = pd.DataFrame({
    "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
    "Experiment": [
    "Particle Collision Analysis","Quantum Entanglement Test","Superconductivity Study","Nuclear Fusion Simulation","Gravitational Wave Detection"],
    "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2024-01-01", periods=5),
    "Date": pd.date_range(start="2023-01-01", periods=5),
})

astronomy_data = pd.DataFrame({
    "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
    "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
    "Brightness (Magnitude)": [-3.0, -3.6, -1.4, 0.2, -11.7],
    "Observation Date": pd.date_range(start="2023-04-12", periods=5),
})

weather_data = pd.DataFrame({
climate_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
@@ -38,18 +39,19 @@
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Dr. Jane Doe"
    field = "Astrophysics"
    institution = "University of Science"
    name = "Tshiololi Tshedza"
    field = "MATHS AND APPILED MATHS"
    institution = "University of Venda"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")

    st.image(
    "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
    caption="Nature (Pixabay)"
        "https://unsplash.com/photos/body-of-water-during-sunset-Xbf_4e7YDII",
    caption="Sunset Over Water (Unsplash)"

)

elif menu == "Publications":
@@ -88,7 +90,7 @@
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose a dataset to explore", 
        ["Physics Experiments", "Astronomy Observations", "Weather Data"]
        ["Physics Experiments", "Astronomy Observations", "climate change Data"]
    )

    if data_option == "Physics Experiments":
@@ -106,30 +108,31 @@
        st.write("### Astronomy Observation Data")
        st.dataframe(astronomy_data)
        # Add widget to filter by Brightness
        brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
        brightness_filter = st.slider("Filter by Brightness (Magnitude)", -12.3, 6.0, (-12.3, 6.0))
        filtered_astronomy = astronomy_data[
            astronomy_data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
        ]
        st.write(f"Filtered Results for Brightness Range {brightness_filter}:")
        st.dataframe(filtered_astronomy)

    elif data_option == "Weather Data":
        st.write("### Weather Data")
        st.dataframe(weather_data)
    elif data_option == "climate change Data":
        st.write("### climate change Data")
        st.dataframe(climate_data)
        # Add widgets to filter by temperature and humidity
        temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
        temp_filter = st.slider("Filter by Temperature (°C)", -14.5, 35.1, (-14.5, 35.1))
        humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
        filtered_weather = weather_data[
            weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
            weather_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
        filtered_climate= climate_data[
            climate_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
            climate_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
        ]
        st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
        st.dataframe(filtered_weather)
        st.dataframe(filtered_climate)



elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "jane.doe@example.com"
    st.write(f"You can reach me at {email}.")
    email = "tshedzamudau941@gmail.com"

    st.write(f"You can reach me at {email}.")

