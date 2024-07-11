from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os

import PIL.Image

import google.generativeai as genai

# API Key
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Access the API key
API_KEY = os.getenv('API_KEY')

PROMT = '''Please provide a detailed recipe including the ingredients and step-by-step instructions on how to prepare the dish. If the image is not of a food item, please return an error message indicating that the image is not recognized as food, dont repeat Ingredients.

Please follow this format:

1. **Dish Name**: [Name of the dish]
2. **Ingredients**:
   - [Ingredient 1]
   - [Ingredient 2]
   - [Ingredient 3]
   - ...

3. **Instructions**:
   1. [Step 1]
   2. [Step 2]
   3. [Step 3]
   4. ...

If the image is not of a food item, respond with:
"Error: The image is not recognized as food." '''

genai.configure(api_key=API_KEY)

def generate_recipe_from_image(image_path):

    img = PIL.Image.open(image_path)
    model = genai.GenerativeModel(model_name='gemini-pro-vision')
    response = model.generate_content([PROMT, img], stream=False)

    buffer = []
    for chunk in response:
        for part in chunk.parts:
            buffer.append(part.text)

    return buffer[0]

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png'}

           
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        print(file_path)
        recipe = generate_recipe_from_image(file_path)
        if generate_recipe_from_image == ' Error: The image is not recognized as food.':
            return jsonify({'error': 'The image is not recognized as food'})
        return jsonify({'recipe': recipe})
    return jsonify({'error': 'File type not allowed'})

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)