import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/api/dub', methods=['POST'])
def dub_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video file provided'}), 400
    
    file = request.files['video']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    return jsonify({
        'status': 'success',
        'message': 'បានទទួលវីដេអូរឿងចិន និងកំពុងបកប្រែជាសំឡេងខ្មែរដោយ AI!',
        'video_url': f'/download/{filename}'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
