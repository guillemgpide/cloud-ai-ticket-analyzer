import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Trobar ruta CSV
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, "data", "dataset.csv")

# Load data to Pandas
try:
    df = pd.read_csv(csv_path, encoding='utf-8')
except FileNotFoundError:
    print(f"⚠️ ERROR: No s'ha trobat el fitxer {csv_path}")
    df = pd.DataFrame(columns=["text", "category", "sentiment"])

# Entrenament
model_category = make_pipeline(TfidfVectorizer(), MultinomialNB())
model_sentiment = make_pipeline(TfidfVectorizer(), MultinomialNB())

if not df.empty:

    model_category.fit(df['text'], df['category'])
    model_sentiment.fit(df['text'], df['sentiment'])

# API
def analyze_ticket(text: str):
    if df.empty:
        return {"category": "Error de Dades", "sentiment": "Unknown", "confidence": "0.0%"}
        
    cat_pred = model_category.predict([text])[0]
    sent_pred = model_sentiment.predict([text])[0]
    
    probabilitats = model_category.predict_proba([text])[0]
    confianca = max(probabilitats) * 100
    
    return {
        "category": cat_pred,
        "sentiment": sent_pred,
        "confidence": f"{round(confianca, 1)}%"
    }