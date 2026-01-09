import pandas as pd
import streamlit as st
import plotly.express as px
import time

st.title("Data analysis")
st.write("Allow Excel and CSV:")
uploaded_files = st.file_uploader(
    "Upload files", accept_multiple_files=False, type=["csv", "xlsx", "xls"]
)

if uploaded_files is not None:
    files = uploaded_files
    if files.name.endswith(".csv"):
        df = pd.read_csv(files)
    else:
        df = pd.read_excel(files)
    st.write(f"**File:** {files.name}")
    st.dataframe(df)
    
    
    options = df.columns.tolist()
    st.session_state["df"] = df
    x_col = st.selectbox("Select X-axis column", df.columns)
    y_col = st.selectbox("Select Y-axis column", df.columns)
    st.session_state["x_col"] = x_col
    st.session_state["y_col"] = y_col

Chartkind = st.selectbox(
    "Choose the type you want",
    ("Bar chart", "Scatter chart","Box cart"),
)



if st.button("Create chart"):
    p = st.empty()
    p.progress(0, "Wait for it...")
    time.sleep(.5)
    p.progress(50, "Wait for it...")
    time.sleep(.5)
    p.progress(100, "Wait for it...")
    time.sleep(.5)
    p.empty()
    if Chartkind=="Bar chart":
        fig = px.bar(df, x=x_col, y=y_col)
    elif Chartkind=="Box cart":
        fig= px.box(df, x=x_col, y=y_col)
    else: 
        fig = px.scatter(df, x=x_col, y=y_col)
    st.plotly_chart(fig)
