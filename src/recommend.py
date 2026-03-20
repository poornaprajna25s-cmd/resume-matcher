job_roles = {
    "Web Developer": ["html", "css", "javascript", "react", "node", "mongodb"],
    "Data Analyst": ["python", "sql", "pandas", "numpy", "data analysis"],
    "Machine Learning Engineer": ["python", "machine learning", "scikit-learn", "numpy", "pandas"],
    "Backend Developer": ["python", "node", "sql", "api", "mongodb"],
    "Full Stack Developer": ["html", "css", "javascript", "react", "node", "mongodb", "api"]
}

def recommend_jobs(resume_skills):
    scores = {}

    for role, skills in job_roles.items():
        match = len(set(resume_skills) & set(skills)) / len(skills)
        scores[role] = round(match * 100, 2)

    # Sort roles by score
    sorted_roles = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return sorted_roles