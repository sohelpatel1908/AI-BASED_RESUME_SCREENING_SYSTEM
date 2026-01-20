from sklearn.metrics.pairwise import cosine_similarity


def similarity_matcher(embed_resume, embed_job_desc):
    
    similarity_score = cosine_similarity(embed_job_desc, embed_resume)

    print(similarity_score)
    return(similarity_score)
