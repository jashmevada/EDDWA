from flask import (Blueprint, request, session, flash, redirect, url_for, render_template)
from werkzeug.utils import secure_filename

from db.db import db
from models.model import *

bp = Blueprint('auth', __name__, url_prefix='/forest_fire')

model = load_model('C:\\Users\\Nikunj\\Desktop\\Space PROj\\models\\fine_tuned_flood_detection_model.h5')

ALLOWED_EXTENSIONS = {'png','jpg','jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(img_path):
    """Preprocess the uploaded image to the required format for the model."""
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return tf.keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)

@bp.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        image = ''
        file = request.files['file']
        print(file)
        filename =  secure_filename(file.filename)

        if file and allowed_file(file.filename):
            session['image'] = file.filename
            file.save(os.path.join("static/upload", filename))

            processed_image =    preprocess_image(os.path.join("static/upload", filename))
            prediction = model.predict(processed_image)
            prediction_class = np.argmax(prediction, axis=1)[0]
            labels = ['Flooding', 'No Flooding']
            result = labels[prediction_class]

            print(preprocess_image)
            print (result)
            return render_template('index.html', res=result)
        else:
            return redirect('detections/forest_fire.html')

    return render_template('detections/forest_fire.html')
