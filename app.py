import streamlit as st
from PIL import Image
import dill
from src.pipeline.predict_pipeline import PredictPipeline
from src.pipeline.preprocess_pipeline import data_transform

def predict(testimg):
    try:    
        predictor = PredictPipeline()
        preds = predictor.predict(testimg)
        pred_age = int(preds)
        st.success(f'Predicted age: {pred_age}')
        return pred_age
    except:
        st.title(' ')
        

# model = joblib.load('xgbpipe.joblib')
st.title("Upload the photo and then click 'Predict the age' ")

try:
    trigger = st.button('Predict the age', on_click=predict(file))
except:
    file = st.file_uploader(" ")
    trigger = st.button('Predict the age', on_click=predict(file))


try:
    image = Image.open(file)
    st.image(image, use_column_width=True)
except:
    st.title(' ')


