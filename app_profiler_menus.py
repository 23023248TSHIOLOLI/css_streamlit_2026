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

# Function to load an image from URL
def load_image(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

# Example image URL (replace with your own image if needed)
image_url = "https://raw.githubusercontent.com/23023248TSHIOLOLI/css_streamlit_2026/main/jay-antol-Xbf_4e7YDII-unsplash.jpg"
image = load_image(image_url)

# Display image in Streamlit
st.image(image, caption="Researcher or Featured Image", use_column_width=True)

# Dummy STEM Data
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
    "Brightness (Magnitude)": [-3.0, -3.6, -1.9, 0.5, -12.7],
    "Observation Date": pd.date_range(start="2023-06-01", periods=5),
})

# Page Content based on Menu Selection
if menu == "Researcher Profile":
    st.header("Researcher Profile")
    st.write("This section can include personal information, biography, and research interests.")

elif menu == "Publications":
    st.header("Publications")
    st.write("List your recent publications or journals in this section.")

elif menu == "STEM Data Explorer":
    st.header("STEM Data Explorer")
    
    # Toggle Tabs for Physics and Astronomy
    tab1, tab2 = st.tabs(["Physics Data", "Astronomy Data"])

    with tab1:
        st.subheader("Physics Experiments")
        st.dataframe(physics_data)
        st.bar_chart(physics_data.set_index("Experiment")["Energy (MeV)"])

    with tab2:
        st.subheader("Astronomy Observations")
        st.dataframe(astronomy_data)
        st.line_chart(astronomy_data.set_index("Celestial Object")["Brightness (Magnitude)"])

elif menu == "Contact":
    st.header("Contact")
    st.write("Include a form or contact details for inquiries here.")

# Footer
st.write("---")
st.write("Developed with ❤️ using Streamlit, Python, and Pillow (PIL).")

# Optional Usage Instructions
st.info("You can replace the image URL with your own or add more images as needed. Adjust data for real STEM datasets.")
