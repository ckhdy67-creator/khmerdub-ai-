import os
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# OpenAI API Key របស់បង
client = OpenAI(api_key="Sk-proj-SPR-mkg68xZCPUOkpJPNNBt6HfIZ8HD5rsyymv_IoFEDJcstIepNgGmRCHDttxlBA0aVvKonM8T3BlbkFJusG9ThvikRGOWsfvllvbOXBy3QXF92vHi50JhyTeXnMMmHJ4OJzHnCAH2TpPJycuvRUApfG8YA")

@app.route('/')
def home():
    return "HELLO, WORLD! KhmerDub AI Server is Ready!"

@app.route('/api/dub', methods=['POST'])
def dub_video():
    try:
        if 'video' not in request.files:
            return jsonify({'error': 'No video file provided'}), 400
        
        video_file = request.files['video']
        
        return jsonify({
            'success': True,
            'message': 'បានទទួលវីដេអូរឿងចិន និងកំពុងបប្រែជាសំឡេងខ្មែរដោយ AI!',
            'filename': video_file.filename
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
