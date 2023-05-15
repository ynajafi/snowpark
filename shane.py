import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

st.header('SHANES COOL AIRPLANE APP')

FILE = st.file_uploader('CHOOSE YOUR FILE (CSV FORMAT)', type='csv')

if 'df' not in st.session_state:
    st.session_state['df'] = None
if 'm_df' not in st.session_state:
    st.session_state['m_df'] = None

if st.button('SAMPLE DATA'):
    st.write("Sample Dataset - 10 Rows")
    file_df = pd.read_csv(FILE)
    st.session_state['df'] = file_df.head(10)
    st.dataframe(st.session_state['df'])

if st.checkbox('more info'):
    if st.session_state['df'] is not None:
        st.session_state['m_df'] = st.session_state['df'].describe()
        st.write(st.session_state['m_df'].T)

# Display column data if dataframe is loaded
if st.session_state['df'] is not None:
    st.subheader('Select Columns')
    columns = st.multiselect('Select Columns of Interest', st.session_state['df'].columns)
    selected_data = st.session_state['df'][columns]
    st.dataframe(selected_data)


# Create scatter plot if dataframe is loaded
if st.session_state['df'] is not None:
    st.subheader('Scatter Plot')
    columns = st.multiselect('Select Columns for Scatter Plot', st.session_state['df'].columns)
    selected_data = st.session_state['df'][columns]
    sns.scatterplot(data=selected_data)
    plt.xlabel(columns[0])
    plt.ylabel(columns[1])
    st.pyplot()