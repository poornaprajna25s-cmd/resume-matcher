skills_list = [
    "python", "java", "c++", "sql", "machine learning",
    "data analysis", "pandas", "numpy", "scikit-learn",
    "javascript", "react", "node", "mongodb", "html", "css",
    "git", "github", "api"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []
    
    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)
    
    return list(set(found_skills))  # remove duplicates


def skill_gap(resume_skills, job_skills):
    return list(set(job_skills) - set(resume_skills))