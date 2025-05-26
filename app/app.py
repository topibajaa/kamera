from flask import Flask, request, render_template
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('kamera.html')  # render halaman kamera

@app.route('/upload', methods=['POST'])
def upload_image():
    image = request.files.get('image')
    if image:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'frame_{timestamp}.jpg'
        path = os.path.join(UPLOAD_FOLDER, filename)
        image.save(path)
        return 'OK', 200
    return 'Gagal', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
