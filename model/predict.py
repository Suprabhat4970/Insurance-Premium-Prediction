import pickle
from pathlib import Path
import pandas as pd

with open('model/model_v6.pkl','rb') as f:
    model = pickle.load(f)

    
MODEL_VERSION = '1.0.0'
class_labels = model.classes_.tolist()

def predict_output(user_input: dict):

    df = pd.DataFrame([user_input])

    predicted_class = model.predict(df)[0]
    
    #get probabilities for all classes
    probabilities = model.predict_proba(df)[0]
    confidence =max(probabilities)

    #create mapping: (class_name: probability)
    class_probs= dict(zip(class_labels,map(lambda p: round(p,4), probabilities)))
    return {
        "predicted_class": predicted_class,
        "confidence": round(confidence,4),
        "class_probabilities": class_probs
    }
