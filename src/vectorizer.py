import os
from sentence_transformers import SentenceTransformer 

MODEL_PATH = "models\\embedding_model"


def loading_model():
    try:
        if os.path.exists(MODEL_PATH):
            model = SentenceTransformer(MODEL_PATH)
            print("\nModel Loaded!\n")
        else:
            model = SentenceTransformer('all-MiniLM-L6-v2')
            model.save(MODEL_PATH)
            print("Model Saved Successfully!!!")
            
        return model
    
    except:
        print("Model Loading Failed!!!")


# Initialize the model once
model = loading_model()


def embedding(content):
    try:
        embedding_text = model.encode([content])
        print(embedding_text, "\n")

        return embedding_text
    
    except Exception as exp:
        print("Error!!!: ", exp)
