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
        
        # រក្សាទុកវីដេអូបណ្តោះអាសន្នក្នុង Server
        upload_dir = './uploads'
        os.makedirs(upload_dir, exist_ok=True)
        file_path = os.path.join(upload_dir, video_file.filename)
        video_file.save(file_path)
        
        # ផ្ញើឯកសារទៅកាន់ OpenAI Whisper API ដើម្បីស្តាប់និងបកប្រែ
        with open(file_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="text"
            )
        
        # លុបហ្វាលចោលវិញដើម្បីកុំឱ្យពេញ Server
        os.remove(file_path)
        
        return jsonify({
            'success': True,
            'message': 'បកប្រែជោគជ័យដោយ AI!',
            'translation': transcript
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
