import dill
from PIL import Image
import sys
from src.exception import CustomException
from src.pipeline.preprocess_pipeline import data_transform

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,file):
        try:
            
            with open('model.pkl', 'rb') as f:
                model = dill.load(f)
            
            img = Image.open(file)
            trans = data_transform()
            t1 = trans.tensorize(img)
            t1 = t1.unsqueeze(0)
            
            return model(t1)
        
        except Exception as e:
            raise CustomException(e,sys)