from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from google.cloud import translate_v2
from google.cloud import texttospeech
import os
import json

app = Flask(__name__)
CORS(app)

# Initialize Google Cloud clients
# Make sure to set GOOGLE_APPLICATION_CREDENTIALS environment variable
try:
    translate_client = translate_v2.Client()
    tts_client = texttospeech.TextToSpeechClient()
except Exception as e:
    print(f"Warning: Google Cloud credentials not configured. Using fallback translation. Error: {e}")
    translate_client = None
    tts_client = None

# Fallback translation dictionary for common words (when Google Cloud is not available)
FALLBACK_TRANSLATIONS = {
    "hello": "ನಮಸ್ಕಾರ",
    "good morning": "ಶುಭೋದಯ",
    "thank you": "ಧನ್ಯವಾದ",
    "yes": "ಹೌದು",
    "no": "ಇಲ್ಲ",
    "goodbye": "ವಿದಾಯ",
    "how are you": "ನೀವು ಹೇಗಿದ್ದೀರಿ",
    "what is your name": "ನಿಮ್ಮ ಹೆಸರು ಏನು",
    "my name is": "ನನ್ನ ಹೆಸರು",
    "please": "ದಯವಿಟ್ಟು",
    "sorry": "ಕ್ಷಮಿಸಿ",
    "welcome": "ಸ್ವಾಗತ",
}

@app.route('/translate', methods=['POST'])
def translate_text():
    """Translate English text to Kannada"""
    try:
        data = request.json
        english_text = data.get('text', '').strip()
        
        if not english_text:
            return jsonify({'error': 'Text is required'}), 400
        
        if translate_client:
            # Use Google Cloud Translation
            result = translate_client.translate_text(
                source_language='en',
                target_language='kn',
                values=[english_text]
            )
            kannada_text = result['translations'][0]['translatedText']
        else:
            # Use fallback translation
            kannada_text = FALLBACK_TRANSLATIONS.get(
                english_text.lower(),
                f"[Translation not available: {english_text}]"
            )
        
        return jsonify({
            'success': True,
            'english': english_text,
            'kannada': kannada_text
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    """Convert text to speech (Kannada)"""
    try:
        data = request.json
        kannada_text = data.get('text', '').strip()
        
        if not kannada_text:
            return jsonify({'error': 'Text is required'}), 400
        
        if not tts_client:
            return jsonify({'error': 'Text-to-speech service not available'}), 503
        
        synthesis_input = texttospeech.SynthesisInput(text=kannada_text)
        voice = texttospeech.VoiceSelectionParams(
            language_code='kn-IN',
            name='kn-IN-Standard-A'
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
        
        response = tts_client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config
        )
        
        # Return audio content as base64
        import base64
        audio_content = base64.b64encode(response.audio_content).decode('utf-8')
        
        return jsonify({
            'success': True,
            'audio': audio_content,
            'mime_type': 'audio/mpeg'
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
