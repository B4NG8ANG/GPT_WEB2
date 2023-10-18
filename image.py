from flask import Flask, render_template, request
from PIL import Image
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('upload.html', image_path=None)

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_image = request.files['image']
    if uploaded_image.filename != '':
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_image.filename)
        uploaded_image.save(image_path)

        # Image analysis code using Pillow (PIL)
        image = Image.open(image_path)
        # Add your analysis code here
        # For example: image = image.convert('L')

        return render_template('upload.html', image_path=image_path)
    return render_template('upload.html', image_path=None)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
