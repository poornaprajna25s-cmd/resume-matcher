from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_match_score(resume, job, resume_skills, job_skills):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume, job])
    
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    # Skill match score
    if len(job_skills) > 0:
        skill_match = len(set(resume_skills) & set(job_skills)) / len(job_skills)
    else:
        skill_match = 0

    # Combine scores
    final_score = (0.6 * similarity) + (0.4 * skill_match)

    # 🎯 Bonus if all skills match
    if skill_match == 1.0:
        final_score += 0.1   # ✅ properly indented

    return round(final_score * 100, 2)