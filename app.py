from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
import io
from PIL import Image

app = Flask(__name__)

# Load the pre-trained Keras model
model = load_model('cats_and_dogs_classifier.h5')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        try:
            # Convert the FileStorage object to an image
            image = Image.open(io.BytesIO(file.read()))
            image = image.resize((150, 150))  # Resize the image to match your model's input size
            image = img_to_array(image)
            image = np.expand_dims(image, axis=0)
            image = image / 255.0  # Normalize the image

            # Make prediction
            prediction = model.predict(image)
            predicted_class = (prediction > 0.5).astype("int32")

            # Map the predicted class to the corresponding label
            labels = ['Cat', 'Dog']  # Adjust these labels according to your model's class_mode
            result = labels[predicted_class[0][0]]

            return jsonify({'prediction': result})
        except Exception as e:
            # Log the exception with detailed information
            print(f"Error processing the image: {e}")
            return jsonify({'error': 'Error processing the image', 'message': str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
