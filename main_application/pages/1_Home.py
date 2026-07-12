import streamlit as st
from utils import helper

students = helper.get_students()

st.markdown(
    "<h1 style='text-align: center; font-size: 50px;'>Software Testing and Quality Assurance - SAT312</h1>",
    unsafe_allow_html=True
)

st.image(
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnKWtNpGi6B2Gs8V2qYe0Sy-C2SlG9SWYbJKskObZSj3Fj-WPHv2fkIIE9&s=10", 
    width="stretch"
)

if not students:
    st.info("No students found.")
else:
    top = helper.highest_score(students)
    low = helper.lowest_score(students)
    avg = helper.get_average_score(students)

    col1, col2, col3 = st.columns(3)
    col1.metric("🏆 Highest Score", f"{top['score']}", top["name"])
    col2.metric("📉 Lowest Score", f"{low['score']}", low["name"])
    col3.metric("📊 Average Score", f"{avg:.1f}")

st.markdown(
    "<p style='text-align: center; font-size: 16px'>A hands-on introduction to software testing and "
    "quality assurance, covering test planning, manual and automated testing, and defect tracking. "
    "View enrolled students and performance in this course below.</p>",
    unsafe_allow_html=True
)

st.write("")

st.write("")

_, cta_col, _ = st.columns([1, 1, 1])
with cta_col:
    if st.button("View all students →", width="stretch", type="primary"):
        st.switch_page("pages/2_Dashboard.py")

st.divider()