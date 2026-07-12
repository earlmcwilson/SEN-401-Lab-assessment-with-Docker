import streamlit as st
from utils import helper

st.header("Students enrolled in SAT312")

all_students = helper.get_students()


departments = ["All"] + helper.get_departments(all_students)
selected_dept = st.selectbox("Filter by department", departments)

students = (
    all_students
    if selected_dept == "All"
    else helper.filter_by_department(all_students, selected_dept)
)


if not students:
    st.info("No students found for this department.")
else:
    st.caption(
        f"📊 Average score: **{helper.get_average_score(students):.1f}** "
        f"· {len(students)} student(s)"
    )

    for i in range(0, len(students), 2):
        row_students = students[i:i + 2]
        cols = st.columns(2)

        for col, student in zip(cols, row_students):
            with col:
                with st.container(border=True):
                    st.write(f"**Name:** {student['name']}")
                    st.write(f"**Gender:** {student['gender']}")
                    st.write(f"**Score:** {student['score']}")
                    if st.button("View →", key=f"view_{student['id']}"):
                        st.session_state["selected_id"] = student["id"]
                        st.switch_page("pages/3_Student_detail.py")