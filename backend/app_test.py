from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Simple translation dictionary
translations = {
    "hello": "ನಮಸ್ಕಾರ",
    "hi": "ಹಾಯ್",
    "thank you": "ಧನ್ಯವಾದ",
    "thanks": "ಧನ್ಯವಾದ",
    "please": "ದಯವಿಟ್ಟು",
    "sorry": "ಕ್ಷಮಿಸಿ",
    "yes": "ಹೌದು",
    "no": "ಇಲ್ಲ",
    "goodbye": "ವಿದಾಯ",
    "good morning": "ಶುಭೋದಯ",
    "welcome": "ಸ್ವಾಗತ",
}

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text', '').lower().strip()
    
    if not text:
        return jsonify({'success': False, 'error': 'Text required'}), 400
    
    kannada = translations.get(text, f"Translation not available for: {text}")
    
    return jsonify({
        'success': True,
        'english': text,
        'kannada': kannada
    }), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'message': 'Backend is working!'}), 200

if __name__ == '__main__':
    print("\n" + "="*50)
    print("English to Kannada Translator Backend")
    print("="*50)
    print("Running on: http://localhost:5000")
    print("Endpoints:")
    print("  - POST /translate (for translations)")
    print("  - GET /health (health check)")
    print("="*50 + "\n")
    app.run(debug=False, host='0.0.0.0', port=5000, use_reloader=False)
