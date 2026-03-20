import streamlit as st
import pandas as pd
from src.matcher import get_match_score
from src.parser import extract_text_from_pdf
from src.skills import extract_skills, skill_gap
from src.recommend import recommend_jobs

# 🎨 Pastel + Vibrant UI Styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #EEF2FF, #FDEFF9);
}

h1 {
    color: #3A0CA3;
    text-align: center;
    font-weight: 700;
}

h2, h3 {
    color: #4361EE;
}

.block-container {
    padding: 2rem;
    border-radius: 15px;
    background-color: rgba(255, 255, 255, 0.8);
}

.stButton>button {
    background: linear-gradient(90deg, #A5B4FC, #FBCFE8);
    color: black;
    border-radius: 10px;
    border: none;
}

.stAlert-success {
    background-color: #E6F9F0;
}

.stAlert-warning {
    background-color: #FFF4E5;
}

.stAlert-error {
    background-color: #FDECEA;
}
</style>
""", unsafe_allow_html=True)

# 🎯 Title
st.title("✨ AI Resume Matcher")

# 📄 Inputs
resume_file = st.file_uploader("📄 Upload Resume (PDF)")
job = st.text_area("💼 Paste Job Description")

# 🔥 MAIN LOGIC (IMPORTANT: everything inside this block)
if resume_file and job:

    # 📄 Extract resume text
    resume_text = extract_text_from_pdf(resume_file)

    # 🧠 Extract skills
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job)

    # ❌ Missing skills
    missing = skill_gap(resume_skills, job_skills)

    # 🎯 Match score
    score = get_match_score(resume_text, job, resume_skills, job_skills)

    # 📊 Show score
    st.subheader(f"📊 Match Score: {score}%")

    # 🎯 SMART FEEDBACK
    if len(missing) == 0:
        st.success("🎉 Excellent! You meet all required skills.")

        if score < 75:
            st.info("💡 Tip: Improve resume wording to increase match score.")

    elif score > 70:
        st.success("🔥 Strong match! You are highly suitable for this role.")

    elif score > 50:
        st.warning("⚠️ Moderate match. Consider improving some skills.")

    else:
        st.error("❌ Low match. Consider improving your skills.")

    # 📊 Chart
    if len(job_skills) > 0:
        skill_match_percent = (len(resume_skills) - len(missing)) / len(job_skills) * 100
    else:
        skill_match_percent = 0

    chart_data = pd.DataFrame({
        "Category": ["Match Score", "Skill Match"],
        "Value": [score, skill_match_percent]
    })

    st.bar_chart(chart_data.set_index("Category"))

    # 📦 Skills display
    col1, col2 = st.columns(2)

    with col1:
        st.write("### ✅ Skills in Resume")
        st.write(resume_skills)

    with col2:
        st.write("### 📌 Skills Required")
        st.write(job_skills)

    # ❌ Missing skills
    st.write("### ❌ Missing Skills")
    if missing:
        st.write(missing)
    else:
        st.success("No missing skills 🎉 You are a great match!")

    # 🎯 Job recommendations
    st.write("## 🎯 Recommended Job Roles")

    recommended = recommend_jobs(resume_skills)

    for role, match_score in recommended[:3]:
        st.write(f"💼 {role} → {match_score}% match")