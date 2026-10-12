# Custom Local Resume Matcher & Keyword Analyzer
import re
import json

def clean_text(text):
"""Cleans raw text inputs for precise keyword matching."""
text = text.lower()
text = re.sub(r'[^a-z0-9\s]', ' ', text)
return set(text.split())

def calculate_match(resume_text, job_description):
"""Analyzes medical qualifications against target role requirements."""
resume_words = clean_text(resume_text)
job_words = clean_text(job_description)

# Core tracking keywords for healthcare AI & clinical roles
target_keywords = {
'mbbs', 'guntur', 'clinical', 'medical', 'triage', 'diagnosis', 'rlhf',
'annotation', 'llm', 'prompt', 'telugu', 'bilingual', 'ehr', 'chart'
}

# Filter job post criteria to meaningful evaluation markers
required_skills = job_words.intersection(target_keywords)
matched_skills = required_skills.intersection(resume_words)
missing_skills = required_skills.difference(resume_words)

# Calculate analytical score
if not required_skills:
score = 0.0
else:
score = round((len(matched_skills) / len(required_skills)) * 100, 2)

results = {
"Match Percentage": f"{score}%",
"Identified Role Requirements Found": list(matched_skills),
"Missing Profile Keywords to Add": list(missing_skills)
}
return json.dumps(results, indent=4)

if __name__ == "__main__":
# Test Baseline Setup
sample_resume = "MBBS graduate from Guntur Medical College. Experienced in clinical triage, patient assessment, RLHF evaluation, and bilingual Telugu translation."
sample_job = "Looking for a Bilingual Medical Expert for Clinical AI Training. Must understand RLHF, annotation, and hold an MBBS degree."

print("--- Running Local Analysis Test ---")
print(calculate_match(sample_resume, sample_job))
