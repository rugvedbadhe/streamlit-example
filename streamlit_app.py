import streamlit as st
import pandas as pd

# Create a Streamlit app
st.title("CSV Explorer Web App")

# Sidebar - CSV File Upload
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Create tabs for different sections
    tabs = st.selectbox("Select a Tab:", ["Overall Info", "DataFrame"])

    if tabs == "Overall Info":
        # Display overall dataset information
        st.write("## Overall Information")
        st.write(f"Number of Rows: {df.shape[0]}")
        st.write(f"Number of Columns: {df.shape[1]}")
        st.write(f"Number of Duplicated Rows: {df.duplicated().sum()}")
        st.write(f"Number of Rows with Missing Values: {df.isnull().any(axis=1).sum()}")

    elif tabs == "DataFrame":
        # Display DataFrame tab
        st.write("## DataFrame")

        # Display the list of columns, data types, and memory usage
        col_info = pd.DataFrame({
            "Column Name": df.columns,
            "Data Type": df.dtypes,
            "Memory Usage": df.memory_usage() / 1024,  # Convert to kilobytes
        })
        st.write("### Column Information")
        st.write(col_info)

        # Interactive options for exploring the dataset
        st.write("### Explore the Dataset")
        num_rows_to_display = st.slider("Select the number of rows to display (5 to 50)", 5, 50)
        display_logic = st.radio("Select how to display rows:", ["Head", "Tail", "Sample"])
        
        if display_logic == "Head":
            st.write(df.head(num_rows_to_display))
        elif display_logic == "Tail":
            st.write(df.tail(num_rows_to_display))
        elif display_logic == "Sample":
            st.write(df.sample(num_rows_to_display))
