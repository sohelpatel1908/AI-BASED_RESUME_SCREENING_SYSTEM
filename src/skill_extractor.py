import pandas as pd
import re

def preprocessing_text(text):
    text = str(text).lower()
    text = re.sub(r'(and )', "", text)
    text = re.sub(r'[\d]', "", text)
    text = re.sub(r'[^\w\d\s.,\-/\'+@#]', " ", text)  
    text = re.sub(r"(\s{2,})", " ", text)
    text = text.strip()
    return text


def load_skills(job_title):
    '''Loading all skills from the Dataset'''

    try:
        skill_db = pd.read_csv('data/job_descriptions/JobsDatasetProcessed.csv')

        skill_list = []

        if 'IT Skills' and 'Soft Skills' in skill_db.columns:
            
            if job_title is not None:    
                if 'IT Skills' in skill_db.columns:
                    for item in skill_db['IT Skills'][skill_db['Job Title'].str.contains(str(job_title).title())]:
                        for items in str(item).lower().split(","):
                            pre_item = preprocessing_text(items)
                            skill_list.append(pre_item)

                if 'Soft Skills' in skill_db.columns:
                    for item in skill_db['Soft Skills'][skill_db['Job Title'].str.contains(str(job_title).title())]:
                        for items in str(item).lower().split(","):
                            pre_item = preprocessing_text(items)
                            skill_list.append(pre_item)

            else:
                if 'IT Skills' in skill_db.columns:
                    for item in skill_db['IT Skills']:
                        for items in str(item).lower().split(","):
                            pre_item = preprocessing_text(items)
                            skill_list.append(pre_item)

                if 'Soft Skills' in skill_db.columns:
                    for item in skill_db['Soft Skills']:
                        for items in str(item).lower().split(","):
                            pre_item = preprocessing_text(items)
                            skill_list.append(pre_item)

        else:
            print("Skill Columns Not Found in JobsDatasetProcessed.csv!!!")

        return set(skill_list)
    
    except Exception as exp:
        print("Error Occurred: ", exp)


def skill_keyword_finder(text, job_title):
    '''Finding all matching skill keywords from load_skills() and given text'''

    skills = load_skills(job_title)
    skill_found = []

    for item in skills:
        if f" {item} " in f" {text} ":
            skill_found.append(item)

    return set(skill_found)


def missing_skill_keywords(job_description, resume, job_title):
    '''Finding missing keywords'''

    jd_skills = skill_keyword_finder(job_description, job_title)
    resume_skills = skill_keyword_finder(resume, job_title)

    missing_skills = jd_skills - resume_skills
    return resume_skills, missing_skills
