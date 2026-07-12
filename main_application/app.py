import streamlit as st 

# Uses st.page to create a page called Home and Dashboard 
home = st.Page("pages/1_Home.py", title="Home")
dashboard = st.Page("pages/2_Dashboard.py", title="Dashboard")
student_detail = st.Page("pages/3_Student_detail.py", title="Student_detail")

# st.navigation registers the page variables as pages 
pg = st.navigation([home,dashboard, student_detail], position="hidden")

with st.sidebar:
    st.page_link(home, label="Home")
    st.page_link(dashboard, label="Dashboard")


pg.run()

