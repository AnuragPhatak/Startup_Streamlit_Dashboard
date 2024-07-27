import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('startup_cleaned.csv')

# Set the title of the dashboard
st.title("Startup Dashboard")

# Add a sidebar for navigation
st.sidebar.title("Welcome Anurag")
st.sidebar.markdown("---")  # Add a divider
#st.sidebar.image("https://via.placeholder.com/150", use_column_width=True)  # Add an image (placeholder for now)
st.sidebar.markdown("## Filters")
page = st.sidebar.selectbox("Select a page:", ["Home", "Data", "Visualizations"])

# Define a color palette
colors = sns.color_palette("husl", 8)

if page == "Home":
    st.header("Welcome to the Startup Dashboard")
    st.write("This dashboard provides insights into various aspects of startups.")
elif page == "Data":
    st.header("Startup Data")
    st.write(data)

    st.header("Summary Statistics")
    st.write(data.describe())

    # Additional functionalities
    st.header("Data Filters")
    city = st.selectbox("Select a city", data['city'].unique())
    filtered_data = data[data['city'] == city]
    st.write(filtered_data)

    vertical = st.multiselect("Select vertical(s)", data['vertical'].unique())
    if vertical:
        filtered_data = data[data['vertical'].isin(vertical)]
        st.write(filtered_data)
elif page == "Visualizations":
    st.header("Visualizations")

    # Visualization: Amount by Round (Top 8 Records)
    st.subheader("Top 8 Investment Amount by Round")
    round_amount = data.groupby('round')['amount'].sum().reset_index()
    round_amount_top8 = round_amount.nlargest(8, 'amount')
    fig, ax = plt.subplots()
    sns.barplot(x='round', y='amount', data=round_amount_top8, ax=ax, palette=colors)
    ax.set_xlabel('Round')
    ax.set_ylabel('Total Investment Amount')
    ax.set_title('Top 8 Total Investment Amount by Round')
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

    # Visualization: Number of Startups by City (Top 8 Records)
    st.subheader("Top 8 Number of Startups by City")
    city_count = data['city'].value_counts().reset_index()
    city_count.columns = ['city', 'count']
    city_count_top8 = city_count.head(8)
    fig, ax = plt.subplots()
    sns.barplot(x='city', y='count', data=city_count_top8, ax=ax, palette=colors)
    ax.set_xlabel('City')
    ax.set_ylabel('Number of Startups')
    ax.set_title('Top 8 Number of Startups by City')
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

    # Visualization: Amount by Vertical (Top 8 Records)
    st.subheader("Top 8 Investment Amount by Vertical")
    vertical_amount = data.groupby('vertical')['amount'].sum().reset_index()
    vertical_amount_top8 = vertical_amount.nlargest(8, 'amount')
    fig, ax = plt.subplots()
    sns.barplot(x='vertical', y='amount', data=vertical_amount_top8, ax=ax, palette=colors)
    ax.set_xlabel('Vertical')
    ax.set_ylabel('Total Investment Amount')
    ax.set_title('Top 8 Total Investment Amount by Vertical')
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

    # Visualization: Number of Startups by Vertical (Top 8 Records)
    st.subheader("Top 8 Number of Startups by Vertical")
    vertical_count = data['vertical'].value_counts().reset_index()
    vertical_count.columns = ['vertical', 'count']
    vertical_count_top8 = vertical_count.head(8)
    fig, ax = plt.subplots()
    sns.barplot(x='vertical', y='count', data=vertical_count_top8, ax=ax, palette=colors)
    ax.set_xlabel('Vertical')
    ax.set_ylabel('Number of Startups')
    ax.set_title('Top 8 Number of Startups by Vertical')
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

# Run the app with `streamlit run startup_dashboard.py`
