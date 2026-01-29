# Alternative Backend for Development/Testing (without Google Cloud)

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import sys

app = Flask(__name__)
CORS(app)

# Comprehensive fallback translation dictionary
TRANSLATIONS_DB = {
    # Greetings
    "hello": "ನಮಸ್ಕಾರ",
    "hi": "ಹಾಯ್",
    "good morning": "ಶುಭೋದಯ",
    "good afternoon": "ಶುಭ ಮಧ್ಯಾಹ್ನ",
    "good evening": "ಶುಭ ಸಂಜೆ",
    "good night": "ಶುಭ ರಾತ್ರಿ",
    "goodbye": "ವಿದಾಯ",
    "see you": "ನಿನ್ನೆ ಭೇಟಿ",
    "welcome": "ಸ್ವಾಗತ",
    
    # Common phrases
    "thank you": "ಧನ್ಯವಾದ",
    "thanks": "ಧನ್ಯವಾದ",
    "please": "ದಯವಿಟ್ಟು",
    "sorry": "ಕ್ಷಮಿಸಿ",
    "excuse me": "ಕ್ಷಮೆಯೇ",
    "yes": "ಹೌದು",
    "no": "ಇಲ್ಲ",
    "okay": "ಸರಿ",
    "ok": "ಸರಿ",
    "sure": "ಖಚಿತವಾಗಿ",
    
    # Questions
    "how are you": "ನೀವು ಹೇಗಿದ್ದೀರಿ",
    "what is your name": "ನಿಮ್ಮ ಹೆಸರು ಏನು",
    "where are you from": "ನೀವು ಎಲ್ಲಿಂದ",
    "how old are you": "ನಿಮ್ಮ ವಯಸ್ಸು ಎಷ್ಟು",
    "what time is it": "ಈಗ ಸಮಯ ಎಷ್ಟು",
    "how much": "ಎಷ್ಟು",
    
    # Useful phrases
    "my name is": "ನನ್ನ ಹೆಸರು",
    "nice to meet you": "ನಿಮ್ಮನ್ನು ಭೇಟಿ ಮಾಡಿ ಖುಷ್ಟಾಗಿದೆ",
    "i love you": "ನಾನು ನಿನ್ನನ್ನು ಪ್ರೀತಿಸುತ್ತೇನೆ",
    "i like you": "ನಾನು ನಿನ್ನನ್ನು ಬಹಳ ಪಸಂದಾಗಿದೆ",
    
    # Food
    "water": "ನೀರು",
    "food": "ಆಹಾರ",
    "coffee": "ಕಾಫಿ",
    "tea": "ಚಾಯ",
    "rice": "ಅನ್ನ",
    "bread": "ಬ್ರೆಡ್",
    
    # Numbers
    "one": "ಒಂದು",
    "two": "ಎರಡು",
    "three": "ಮೂರು",
    "four": "ನಾಲ್ಕು",
    "five": "ಐದು",
    
    # Days
    "monday": "ಸೋಮವಾರ",
    "tuesday": "ಮಂಗಳವಾರ",
    "wednesday": "ಬುಧವಾರ",
    "thursday": "ಗುರುವಾರ",
    "friday": "ಶುಕ್ರವಾರ",
    "saturday": "ಶನಿವಾರ",
    "sunday": "ರವಿವಾರ",
}

def find_best_match(english_text):
    """Find best matching translation for input text"""
    text_lower = english_text.lower().strip()
    
    # Exact match
    if text_lower in TRANSLATIONS_DB:
        return TRANSLATIONS_DB[text_lower]
    
    # Check if input contains any known phrases
    for key, value in TRANSLATIONS_DB.items():
        if key in text_lower:
            return value
    
    # No match found
    return f"[Translation not available for: {english_text}]"

@app.route('/translate', methods=['POST'])
def translate_text():
    """Translate English text to Kannada (Fallback version)"""
    try:
        data = request.json
        english_text = data.get('text', '').strip()
        
        if not english_text:
            return jsonify({'error': 'Text is required'}), 400
        
        kannada_text = find_best_match(english_text)
        
        return jsonify({
            'success': True,
            'english': english_text,
            'kannada': kannada_text
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'ok',
        'mode': 'fallback',
        'translations_available': len(TRANSLATIONS_DB)
    }), 200

@app.route('/translations', methods=['GET'])
def get_available_translations():
    """Get all available translations"""
    return jsonify({
        'total': len(TRANSLATIONS_DB),
        'translations': TRANSLATIONS_DB
    }), 200

if __name__ == '__main__':
    print("Starting English to Kannada Translator (Fallback Mode)")
    print(f"Available translations: {len(TRANSLATIONS_DB)}")
    print("Endpoints:")
    print("  POST /translate - Translate English to Kannada")
    print("  GET /health - Health check")
    print("  GET /translations - View all translations")
    app.run(debug=True, host='0.0.0.0', port=5000)
