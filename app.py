import streamlit as st
from src.parser import pdf_parser
from src.preprocess import preprocessing
from src.matcher import similarity_matcher
from src.vectorizer import embedding
from src.ranker import ranking_files
from src.skill_extractor import missing_skill_keywords
import pandas as pd
import time
import os
 

# Page Configuration Setup
st.set_page_config(page_title="AI Resume Screener", page_icon="🤖")
st.title(":rainbow[**Resume Screening System**]")
st.write("**Upload a resume and paste a job description to see the match score!**")
st.caption("**Note:** :green[Add Job Title for better results!]")

# Header & Sidebar for Job Description
st.header("Upload Resume")
# st.sidebar.header(":rainbow[**Job Title**]")
st.sidebar.header(":rainbow[**Job Title**  &  **Job Description**]")

# A. Input Layer --> (Getting Resume and Job Description from the user)
job_title = st.sidebar.text_input("**(OPTIONAL) Enter Job Title in Full Form:**", placeholder="Enter Exact or Related Job Title")
job_description = st.sidebar.text_area("**Enter Job Description here:**", height=500)
uploaded_files = st.file_uploader("Choose a file", type="pdf", accept_multiple_files=True)

if st.button("Calculate Similarity Score!", icon="🔥"):
    
    if uploaded_files is not None and job_description:
        file_scores = {'File': [], 'Scores': [], 'Grade': [],}

        with st.spinner('Analyzing...'): 
            # # Save and Access file details
            # print("\nSaving file into data/resumes/...")
            # save_pdf = os.path.join('data\\resumes', uploaded_file.name)

            # Pre-processing Job Description --> (So, we don't have to embed again and again)
            preprocessed_jd = preprocessing(job_description)
            print(preprocessed_jd)

        # B. Document Parsing Layer, NLP Preprocessing, Feature Representation, Similarity Engine, Ranking Engine
            for file in uploaded_files:
                # 1. Parsing content from the file     
                file_content = pdf_parser(file)

                # 2. Pre-processing file content
                pre_processing = preprocessing(file_content)
                print(pre_processing)

                # 3. Vectorizing the content
                emb_resume = embedding(pre_processing)
                emb_jd = embedding(preprocessed_jd)

                # 4. Matching Similarity Score
                similarity_score = similarity_matcher(emb_jd, emb_resume)
                match_percentage = round(similarity_score[0][0] * 100, 2)
            
                # 5. Ranking Files with Scores
                file_scores["File"].append(file.name)
                file_scores["Scores"].append(match_percentage)
                if similarity_score[0][0] >= 0.80:
                    file_scores["Grade"].append("Strong Match")
                elif (similarity_score[0][0] >= 0.60) and (similarity_score[0][0] < 0.80):
                    file_scores["Grade"].append("Qualified")
                elif (similarity_score[0][0] >= 0.40) and (similarity_score[0][0] < 0.60):
                    file_scores["Grade"].append("Weak Match/Recheck Resume")
                else:
                    file_scores["Grade"].append("No Match!")
            
                # 6. Extracting and finding missing Skills
                founded_resume_skills, missing_skills = missing_skill_keywords(preprocessed_jd, pre_processing, job_title)

                with st.expander(f"Skill Details for **{file.name}** (**Score: {match_percentage}%**)"):
                    st.write(f"**Keywords/Skills Found:** {', '.join(founded_resume_skills).title()}")
                    if missing_skills:
                        st.error(f"**Missing Keywords:** {', '.join(missing_skills).title()}")
                    else:
                        st.success("All required skills found!")


        # C. Output Layer --> (Getting Ranking Table with file Scores)
        st.success("Analysis Complete!")
        ranked_pdf = ranking_files(file_scores)

        st.dataframe(ranked_pdf, use_container_width=True)
        st.snow()

    else:
        st.warning("Please Upload both **Resume** and **Job Description**!", icon="🚨")