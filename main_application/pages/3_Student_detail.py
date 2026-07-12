import streamlit as st
from utils import helper

student, error = helper.get_validated_student(st.session_state.get("selected_id"))

if error or not student:
    st.error(error or "Student not found.")
    if st.button("← Back to Students"):
        st.switch_page("pages/2_Dashboard.py")
    st.stop()

st.divider()

img_col, info_col = st.columns([1, 2])

with img_col:
    if student["profile_image"]:
        st.image(str(student["profile_image"]))
    else:
        st.image("https://placehold.co/200x200?text=No+Photo")  # fallback placeholder

with info_col:
    st.markdown(f"## {student["name"]}")
    st.caption(f"{student["department"]} · {student["matric_no"]}")

    badge_color = "green" if student["score"] >= 75 else "orange" if student["score"] >= 50 else "red"
    st.markdown(f":{badge_color}[**Score: {student["score"]}**]")

st.divider()

with st.container(border=True):
    c1, c2 = st.columns(2)
    with c1:
        st.write(f"Gender: {student["gender"]}")
        st.markdown("**Matric Number**")
        st.write(student["matric_no"])
    with c2:
        st.write(f"Department: {student["department"]}")

if st.button("← Back to Students"):
    st.switch_page("pages/2_Dashboard.py")