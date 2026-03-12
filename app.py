import streamlit as st

# ---------------- PAGE CONFIG (MUST BE FIRST) ----------------
st.set_page_config(
    page_title="AI Assistant For Teachers",
    page_icon="🎓",
    layout="wide"
)

# ---------------- IMPORT MODULES ----------------
from teacheranalysis import analysis
from MCQ import MCQ
from LessonPlan import lessonplan
from lessonsummarize import summarize
from wellness import counsellor


# ---------------- HEADER SECTION ----------------
st.markdown(
    """
    <div style='text-align:center; padding-top:10px;'>
        <h1 style='margin-bottom:5px;'>AI Assistant For Teachers</h1>
        <p style='font-size:18px; margin-top:0px;'>
            Smart Academic Analysis & AI Teaching Tools
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()


# ---------------- SIDEBAR NAVIGATION ----------------
st.sidebar.title("Navigation")

options = st.sidebar.selectbox(
    "What would you like to do?",
    [
        "Perform Analysis",
        "Generate Quiz",
        "Generate Lesson Plan / Notes",
        "Summarize Lesson",
        "Get Counselling By AI"
    ]
)


# ---------------- ROUTING ----------------
if options == "Perform Analysis":
    analysis()

elif options == "Generate Quiz":
    MCQ()

elif options == "Generate Lesson Plan / Notes":
    lessonplan()

elif options == "Summarize Lesson":
    summarize()

elif options == "Get Counselling By AI":
    counsellor()