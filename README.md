# Text Translation Web Application

A web application that allows users to translate selected text on a webpage using the DeepL API.

## Features

- Highlight text to translate it
- Support for multiple languages
- Real-time translation
- Maintains original text styling
- Rate limiting to prevent abuse
- Error handling and fallback mechanisms

## Prerequisites

- Python 3.7+
- DeepL API key (get one at [DeepL API](https://www.deepl.com/pro-api))

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your DeepL API key:
```
DEEPL_API_KEY=your-api-key-here
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Select any text on the webpage
2. A translation menu will appear near the selected text
3. Choose the target language from the dropdown menu
4. Click "Translate" to see the translation
5. Hover over translated text to see the original version

## Security Considerations

- API keys are stored in environment variables
- Input sanitization is implemented
- Rate limiting is enabled to prevent abuse
- CORS is configured for security

## Technical Details

- Backend: Flask
- Frontend: Vanilla JavaScript
- Translation: DeepL API
- Rate Limiting: Flask-Limiter
- CORS: Flask-CORS

## Error Handling

The application includes comprehensive error handling for:
- API failures
- Network issues
- Invalid input
- Rate limit exceeded

## Contributing

Feel free to submit issues and enhancement requests! #   Y O U R R E P O  
 #   Y O U R R E P O  
 #   Y O U R R E P O  
 #   Y O U R R E P O  
 #   T R A N S L A T E  
 #   T R A N S L A T E  
 #   T R A N S L A T E  
 #   T R A N S L A T E  
 #   T R A N S L A T E  
 