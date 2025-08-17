from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import MinMaxScaler
from scipy.spatial import distance 

model = SentenceTransformer("modelsaving") 


def get_embeddings(text):
    embeddings = model.encode(text)
    return embeddings


def cosine_similarity(emb1, emb2):
    return 1-distance.cosine(emb1,emb2)

def calculate(text1,text2):
    embedding1 = get_embeddings(text1)
    embedding2 = get_embeddings(text2)
    score = cosine_similarity(embedding1,embedding2)
    return score

app = Flask(__name__)
@app.route('/predict',methods=['POST'])
def predict():
    data = request.get_json(force = True)
    print(data)
    text1 = data['text1']
    text2 = data['text2']
    score = calculate(text1,text2)
    return jsonify({"similarity_score" : score})

if(__name__ =='__main__'):
    app.run(port=4000)