from sentence_transformers import SentenceTransformer
import joblib
model = SentenceTransformer("nli-distilroberta-base-v2")
joblib.dump(model,'data neuron task/model.pkl')