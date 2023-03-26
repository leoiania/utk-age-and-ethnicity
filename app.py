from flask import Flask,request,render_template,flash
from src.pipeline.predict_pipeline import PredictPipeline
import io
import base64
from werkzeug.utils import secure_filename


import PIL


app = Flask(__name__)
app.secret_key = 'secret'



@app.route('/upload',methods=['GET', 'POST'])
def upload():
    if request.method=='GET':
        return render_template('home.html')
    else:
        try:
            file = request.files['image']
            
                        
            predictor = PredictPipeline()
            preds = predictor.predict(file)
            pred_age = int(preds)

            # pic = PIL.Image.open(io.BytesIO(file.read()))
            img = PIL.Image.open(file) 
            data = io.BytesIO()
            img.save(data, "JPEG")
            encoded_img = base64.b64encode(data.getvalue())
            decoded_img = encoded_img.decode('utf-8')
            img_data = f"data:image/jpeg;base64,{decoded_img}"

            return render_template('home.html',pred_age =pred_age,picture=img_data)

        
        except PIL.UnidentifiedImageError:
            flash('Error: Please upload a valid image file.')
            return render_template('home.html',pred_age = '77777')


if __name__=="__main__":
    app.run(debug='True',host="0.0.0.0")     