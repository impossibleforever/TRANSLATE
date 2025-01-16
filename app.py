from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
from dotenv import load_dotenv
from googletrans import Translator

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure rate limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["100 per day", "10 per minute"],
    storage_uri="memory://"
)

# Initialize Google translator
translator = Translator()

@app.route('/translate', methods=['POST'])
@limiter.limit("10 per minute")
def translate():
    try:
        data = request.get_json()
        if not data or 'text' not in data or 'target_lang' not in data:
            return jsonify({'error': 'Missing required parameters'}), 400

        text = data['text']
        target_lang = data['target_lang']

        # Google translate
        result = translator.translate(text, dest=target_lang)
        return jsonify({'translated_text': result.text})

    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True) 