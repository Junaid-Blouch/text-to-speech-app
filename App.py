from flask import Flask, render_template, request, url_for
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_text():
    text = request.form['text']
    
    tts = gTTS(text=text, lang='en', slow=False)
    
    audio_path = "static/output.mp3"
    tts.save(audio_path)

    return render_template("index.html", audio_file="output.mp3")

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
