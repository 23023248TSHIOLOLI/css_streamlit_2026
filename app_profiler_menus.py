# Language: Python

# Necessary imports
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import requests
from io import BytesIO

# Set up Streamlit page
st.set_page_config(page_title="Researcher Profile and STEM Data Explorer", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Publications", "STEM Data Explorer", "Contact"],
)

# Dummy STEM data
physics_data = pd.DataFrame({
    "Experiment": [
        "Particle Collision Analysis",
        "Quantum Entanglement Test",
        "Superconductivity Study",
        "Nuclear Fusion Simulation",
        "Gravitational Wave Detection"
    ],
    "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2023-01-01", periods=5),
})

astronomy_data = pd.DataFrame({
    "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
    "Brightness (Magnitude)": [-3.0, -3.6, -1.4, 0.2, -11.7],
    "Observation Date": pd.date_range(start="2023-04-12", periods=5),
})

# Function to load image from GitHub
def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return Image.open(BytesIO(response.content))
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to load image: {e}")
        return None

# Replace these with your GitHub repo details and raw image link
image_url = "https://raw.githubusercontent.com/<username>/<repository>/main/image.png"

# Display sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.markdown("Welcome to the Researcher Profile section.")
    # Load and display GitHub image
    profile_image = load_image(image_url)
    if profile_image:
        st.image(profile_image, caption="Profile Image from GitHub", use_column_width=True)

elif menu == "Publications":
    st.title("Publications")
    st.table(pd.DataFrame({
        "Title": ["Paper A", "Paper B", "Paper C"],
        "Year": [2021, 2022, 2023]
    }))

elif menu == "STEM Data Explorer":
    st.title("Physics Experiments Data")
    st.dataframe(physics_data)
    st.title("Astronomy Observations Data")
    st.dataframe(astronomy_data)

elif menu == "Contact":
    st.title("Contact")
    st.markdown("You can reach me at [email@example.com](mailto:email@example.com)")

# Optional footer
st.markdown("---")
st.markdown("App built with Streamlit")
