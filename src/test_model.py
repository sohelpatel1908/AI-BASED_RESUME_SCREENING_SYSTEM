from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer 
from sklearn.linear_model import LogisticRegression
from preprocess import preprocessing
from parser import pdf_parser


file = input("Enter path: ")
content = pdf_parser(file)
preprocessed_content = preprocessing(content)
print(preprocessed_content)

model = SentenceTransformer('all-MiniLM-L6-v2')
model2 = LogisticRegression()

# Example Data
job_description = '''📝 Job Description We are looking for a motivated and detail-oriented Fresher Data Analyst to join our team. The ideal candidate should have a strong interest in data analysis, basic statistical concepts, and data visualization. This role is suitable for recent graduates who want to build a career in Data Analytics / Data Science and gain hands-on experience working with real datasets.🔍 Roles & Responsibilities Collect, clean, and preprocess structured and unstructured data Perform Exploratory Data Analysis (EDA) to identify patterns and insights Analyze data using Python, SQL, and Excel Create reports and dashboards using visualization tools Assist in building data-driven solutions to support business decisions Work with cross-functional teams to understand data requirements Maintain data accuracy and documentation Present insights in a clear and understandable manner 🎓 Required Skills & Qualifications
Technical Skills:
Basic knowledge of Python (Pandas, NumPy, Matplotlib/Seaborn) Understanding of SQL queries (SELECT, JOIN, GROUP BY, WHERE) Knowledge of Excel (VLOOKUP/XLOOKUP, Pivot Tables, Charts) Basic understanding of statistics (mean, median, variance) Familiarity with data visualization tools (Power BI / Tableau – optional)
Soft Skills:
Strong analytical and problem-solving skills Good communication skills Willingness to learn and adapt Attention to detail
🌱 Good to Have (Optional)
Knowledge of Machine Learning basics Experience with real-world datasets or academic projects Familiarity with Git/GitHub Understanding of business metrics and KPIs'''
resume_1 = preprocessed_content

embedding_job_description = model.encode([job_description])
embedding_resume_1 = model.encode([resume_1])

# resume_1 = 0.72396266
similarity_resume_1 = cosine_similarity(embedding_job_description, embedding_resume_1)

print(f"\nPercentage of Similarity of Resume 1 with the Job Description:{similarity_resume_1[0][0] * 100: .2f}")
