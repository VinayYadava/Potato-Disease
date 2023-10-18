# Import the library
import argparse
from io import BytesIO
from PIL import Image
import numpy as np
from werkzeug.utils import secure_filename
import tensorflow as tf
from numpy import asarray
import os
# Create the parser
parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument('--image_path', type=str, required=True)
parser.add_argument('--model_path', type=str, required=True)

# Parse the argument
args = parser.parse_args()


MODEL = tf.keras.models.load_model(args.model_path)
SUPPORTED_CLASS_NAMES= {"potato":["Early Blight", "Late Blight", "Healthy"]}
OUTPUT = []
Photo=Image.open(args.image_path)

Photo=asarray(Photo)
Photo=np.reshape(Photo,(256,256,3))
img_batch = np.expand_dims(Photo, 0)
        
predictions = MODEL.predict(img_batch)
        
predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
OUTPUT.append(predicted_class)
confidence = np.max(predictions[0])
OUTPUT.append(confidence)
SRC=full_filename
OUTPUT.append(SRC)
accuracy=confidence*100
OUTPUT.append(accuracy)

print(OUTPUT)