import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Researcher Profile and STEM Data Explorer", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Publications", "STEM Data Explorer", "Contact"],
)

# Dummy STEM data
physics_data = pd.DataFrame({
    "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
    "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2024-01-01", periods=5),
})

maths_data = pd.DataFrame({
    "Topic": [ "Linear Algebra","Differential Equations","Probability Theory","Numerical Methods","Optimization"],
    "Application Area": [ "Machine Learning", "Physics Modeling", "Risk Analysis","Engineering Simulation","Operations Research"],
    "Difficulty Level": [3, 4, 2, 5, 4],
    "Computation Time (s)": [0.5, 1.2, 0.3, 2.5, 1.8],
    "Date": pd.date_range(start="2024-01-01", periods=5),
})


weather_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "TSHIOLOLI TSHEDZA"
    field = "MATHS AND APPLIED MATHS"
    institution = "University of Venda"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    
    st.image(
    "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
    caption="Nature (Pixabay)"
)

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

elif menu == "STEM Data Explorer":
    st.title("STEM Data Explorer")
    st.sidebar.header("Data Selection")
    
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose a dataset to explore", 
        ["Physics Experiments", "Maths Observations", "Weather Data"]
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
elif data_option == "Mathematics & Applied":
    st.write("### Mathematics & Applied Data")
    st.dataframe(maths_data)

    # Filter by difficulty
    difficulty_filter = st.slider(
        "Filter by Difficulty Level",
        min_value=1,
        max_value=5,
        value=(1, 5)
    )

    # Filter by computation time
    time_filter = st.slider(
        "Filter by Computation Time (seconds)",
        min_value=0.0,
        max_value=5.0,
        value=(0.0, 5.0)
    )

    filtered_maths = maths_data[
        maths_data["Difficulty Level"].between(difficulty_filter[0], difficulty_filter[1]) &
        maths_data["Computation Time (s)"].between(time_filter[0], time_filter[1])
    ]

    if filtered_maths.empty:
        st.info("No results match the selected filters.")
    else:
        st.write(
            f"Filtered Results for Difficulty {difficulty_filter} "
            f"and Computation Time {time_filter}:"
        )
        st.dataframe(filtered_maths)

    # Visualization
    st.subheader("Difficulty vs Computation Time")
    st.scatter_chart(
        filtered_maths,
        x="Difficulty Level",
        y="Computation Time (s)"
    )

    

    elif data_option == "Weather Data":
        st.write("### Weather Data")
        st.dataframe(weather_data)
        # Add widgets to filter by temperature and humidity
        temp_filter = st.slider("Filter by Temperature (°C)", -9.0, 34.0, (-10.0, 40.0))
        humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
        filtered_weather = weather_data[
            weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
            weather_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
        ]
        st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
        st.dataframe(filtered_weather)
        
        

elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "tshedzamudau941@gmail.com"
    st.write(f"You can reach me at {email}.")

