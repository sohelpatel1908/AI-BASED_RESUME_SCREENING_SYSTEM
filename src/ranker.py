import pandas as pd

def ranking_files(file_scores):
    try:
        pdf_score = pd.DataFrame(file_scores).sort_values(by='Scores', ascending=False, ignore_index=True)
        print(pdf_score.to_string())
        return pdf_score
    
    except Exception as exp:
        return exp, "Error!!!"