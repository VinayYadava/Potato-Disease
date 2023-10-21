from flask import Flask , render_template , request,redirect,url_for
from io import BytesIO
from PIL import Image
import numpy as np
from werkzeug.utils import secure_filename
import tensorflow as tf
from numpy import asarray
import os
import threading
from pyngrok import ngrok
import cv2

os.environ["FLASK_ENV"] = "development"



SUPPORTED_NAMES=['potato']
STATUS=""
OUTPUT=[]
MODEL = tf.keras.models.load_model("./models/1")
SUPPORTED_CLASS_NAMES= {"potato":["Early Blight", "Late Blight", "Healthy"]}


app = Flask(__name__)
port = 7860
# Open a ngrok tunnel to the HTTP server
public_url = ngrok.connect(port).public_url
print(" * ngrok tunnel \"{}\" -> \"http://0.0.0.0:{}\"".format(public_url, port))

# Update any base URLs to use the public ngrok URL
app.config["BASE_URL"] = public_url



@app.route('/')
def home():
    STATUS=''
    OUTPUT=[]
    return render_template('home.html')
 
@app.route('/diagnose_form')
def diagnose():
    return render_template('diagnose.html' , STATUS=STATUS)

@app.route('/report')
def report():
    STATUS=''
    OUTPUT=[]
    return render_template('report.html')
    
@app.route('/getting_form_data' , methods=["GET","POST"])
def getting_form_data():
    OUTPUT.clear()
    Name=request.form['name']
    Name=Name.lower()
    OUTPUT.append(Name)
    if Name in SUPPORTED_NAMES :
        CLASS_NAMES = SUPPORTED_CLASS_NAMES[Name]
        Photo=Image.open(request.files['image'])
        
        Photo=asarray(Photo)
        Photo=Photo.reshape((256,256,3))
        img_batch = np.expand_dims(Photo, 0)
        
        predictions = MODEL.predict(img_batch)
        
        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        OUTPUT.append(predicted_class)
        confidence = np.max(predictions[0])
        OUTPUT.append(confidence)
        img_base64 = Image.fromarray(Photo.astype('uint8'))
        buffered = BytesIO()
        img_base64.save(buffered, format="JPEG")
        img_base64_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        OUTPUT.append(img_base64_str)
        accuracy=confidence*100
        OUTPUT.append(accuracy)
        return redirect("/prediction_interface")
    return redirect("/error")

@app.route('/prediction_interface')
def prediction_interface():
    return render_template(
                            'prediction_interface.html' ,
                            name=OUTPUT[0],
                            category=OUTPUT[1],
                            confidence=OUTPUT[2],
                            user_image=OUTPUT[3],
                            accuracy=OUTPUT[4]
                        )
    
  

#return render_template('prediction_interface.html' , name=OUTPUT[0],src=OUTPUT[1])
#return render_template('prediction_interface.html' , name=OUTPUT[0],category=OUTPUT[1],confidence=OUTPUT[2],src=OUTPUT[3])
#    return f"{OUTPUT[0]},{OUTPUT[1]},{OUTPUT[2]},{OUTPUT[3]}" 



# Start the Flask server in a new thread
threading.Thread(target=app.run, kwargs={"use_reloader": False}).start()
