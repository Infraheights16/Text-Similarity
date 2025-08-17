from sentence_transformers import SentenceTransformer
model = SentenceTransformer("nli-distilroberta-base-v2") 
model.save("modelsaving")  
print("Model saved successfully!")