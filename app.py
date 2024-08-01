import streamlit as st

st.title('My Jupyter Notebook as a Streamlit App')

# Load the Jupyter notebook
with open('yolocrop.ipynb', 'r') as f:
    notebook = f.read()

st.markdown(notebook, unsafe_allow_html=True)
