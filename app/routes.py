from flask import Blueprint, request, jsonify
from googletrans import Translator

translate_bp = Blueprint('translate', __name__)
translator = Translator()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Translation API</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }
        pre {
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
        }
        code {
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Translation API</h1>
    <p>Welcome to the Translation API service. Below are the usage instructions:</p>
    
    <h2>API Endpoint:</h2>
    <pre><code>POST /translate</code></pre>
    
    <h2>Request Format:</h2>
    <pre><code>{
    "text": "Text to translate",
    "target_lang": "Language code (e.g., 'es' for Spanish)"
}</code></pre>

    <h2>Example Response:</h2>
    <pre><code>{
    "translated_text": "Texto traducido"
}</code></pre>

    <h2>Common Language Codes:</h2>
    <ul>
        <li>'es' - Spanish</li>
        <li>'fr' - French</li>
        <li>'de' - German</li>
        <li>'it' - Italian</li>
        <li>'ja' - Japanese</li>
        <li>'ko' - Korean</li>
        <li>'zh-cn' - Chinese (Simplified)</li>
    </ul>
</body>
</html>
"""

@translate_bp.route('/')
def index():
    return HTML_TEMPLATE, 200, {'Content-Type': 'text/html'}

@translate_bp.route('/translate', methods=['POST'])
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