

# Necessary imports
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import requests
from io import BytesIO

# Set page title
# Set up Streamlit page
st.set_page_config(page_title="Researcher Profile and STEM Data Explorer", layout="wide")

# Sidebar Menu

# Dummy STEM data
physics_data = pd.DataFrame({
    "Experiment": ["Particle Collision Analysis","Quantum Entanglement Test","Superconductivity Study","Nuclear Fusion Simulation","Gravitational Wave Detection"],
      
    "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2023-01-01", periods=5),
})


climate_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
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

# Sections based on menu selection
# Display sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Tshiololi Tshedza"
    field = "MATHS AND APPILED MATHS"
    institution = "University of Venda"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    
    if uploaded_file is not None:
    image = Image.open(uploaded_file)
    else:
    image = Image.open("jay-antol-Xbf_4e7YDII-unsplash.jpg")

    st.image(image, caption="Image Preview", use_container_width=True)


    st.markdown("Welcome to the Researcher Profile section.")
    # Load and display GitHub image
    profile_image = load_image(image_url)
    if profile_image:
        st.image(profile_image, caption="Profile Image from GitHub", use_column_width=True)

elif menu == "Publications":
    st.title("Publications")
    st.sidebar.header("Upload and Filter")

    # Upload publications file
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")

        # Publication trends
        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")
    st.table(pd.DataFrame({
        "Title": ["Paper A", "Paper B", "Paper C"],
        "Year": [2021, 2022, 2023]
    }))

elif menu == "STEM Data Explorer":
    st.title("STEM Data Explorer")
    st.sidebar.header("Data Selection")
    
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose a dataset to explore", 
        ["Physics Experiments", "Astronomy Observations", "climate change Data"]
    )

    if data_option == "Physics Experiments":
        st.write("### Physics Experiment Data")
        st.dataframe(physics_data)
        # Add widget to filter by Energy levels
        energy_filter = st.slider("Filter by Energy (MeV)", 0.0, 10.0, (0.0, 10.0))
        filtered_physics = physics_data[
            physics_data["Energy (MeV)"].between(energy_filter[0], energy_filter[1])
        ]
        st.write(f"Filtered Results for Energy Range {energy_filter}:")
        st.dataframe(filtered_physics)

    elif data_option == "Astronomy Observations":
        st.write("### Astronomy Observation Data")
        st.dataframe(astronomy_data)
        # Add widget to filter by Brightness
        brightness_filter = st.slider("Filter by Brightness (Magnitude)", -12.3, 6.0, (-12.3, 6.0))
        filtered_astronomy = astronomy_data[
            astronomy_data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
        ]
        st.write(f"Filtered Results for Brightness Range {brightness_filter}:")
        st.dataframe(filtered_astronomy)

    elif data_option == "climate change Data":
        st.write("### climate change Data")
        st.dataframe(climate_data)
        # Add widgets to filter by temperature and humidity
        temp_filter = st.slider("Filter by Temperature (°C)", -14.5, 35.1, (-14.5, 35.1))
        humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
        filtered_climate= climate_data[
            climate_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
            climate_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
        ]
        st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
        st.dataframe(filtered_climate)
        
        
    st.title("Physics Experiments Data")
    st.dataframe(physics_data)
    st.title("Astronomy Observations Data")
    st.dataframe(astronomy_data)

elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "tshedzamudau941@gmail.com"

    st.write(f"You can reach me at {email}.")




