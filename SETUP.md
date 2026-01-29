# English to Kannada Translator - Setup Guide

A full-stack web application for translating English text to Kannada with text-to-speech and speech-to-text capabilities.

## 🎯 Features

- ✨ **Text Translation**: Convert English text to Kannada
- 🔊 **Text-to-Speech**: Listen to Kannada pronunciation
- 🎤 **Speech Recognition**: Speak English and get transcribed text
- 📋 **Copy to Clipboard**: Easily copy translated text
- 🎨 **Modern UI**: Clean, responsive, beautiful interface
- ⚡ **Real-time Translation**: Instant feedback

## 📁 Project Structure

```
english-to-kannada-2/
├── backend/
│   ├── app.py                 # Flask API server
│   ├── requirements.txt       # Python dependencies
│   └── .env.example          # Configuration template
├── frontend/
│   ├── index.html            # Web UI
│   ├── styles.css            # Styling
│   └── script.js             # Frontend logic
└── README.md & SETUP.md      # Documentation
```

## 🚀 Quick Start (5 minutes)

### Step 1: Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

✅ Backend runs on http://localhost:5000

### Step 2: Frontend Setup

```bash
cd frontend
python -m http.server 8000
```

✅ Open http://localhost:8000 in your browser

## 📖 Detailed Setup

### Prerequisites
- Python 3.8+
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Optional: Google Cloud Account (for enhanced translation)

### Backend Installation

1. **Create virtual environment**:
   ```bash
   cd backend
   python -m venv venv
   
   # Activate on Windows
   venv\Scripts\activate
   
   # Activate on macOS/Linux
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run server**:
   ```bash
   python app.py
   ```

### Frontend Installation

**Option 1: Python HTTP Server**
```bash
cd frontend
python -m http.server 8000
```

**Option 2: Node.js HTTP Server**
```bash
npm install -g http-server
cd frontend
http-server
```

**Option 3: Direct File Access**
```bash
# Simply open the file in your browser
frontend/index.html
```

## 🔌 API Endpoints

### 1. Translate Text
```
POST /translate
Content-Type: application/json

{
  "text": "Hello, how are you?"
}

Response:
{
  "success": true,
  "english": "Hello, how are you?",
  "kannada": "ನಮಸ್ಕಾರ, ನೀವು ಹೇಗಿದ್ದೀರಿ?"
}
```

### 2. Text-to-Speech
```
POST /text-to-speech
Content-Type: application/json

{
  "text": "ನಮಸ್ಕಾರ"
}

Response:
{
  "success": true,
  "audio": "SUQzBAAAAAAAI1...",
  "mime_type": "audio/mpeg"
}
```

### 3. Health Check
```
GET /health

Response:
{
  "status": "ok"
}
```

## 🌐 Google Cloud Setup (Optional)

For full translation and text-to-speech capabilities:

### 1. Create Google Cloud Project
- Visit https://console.cloud.google.com
- Create a new project
- Enable billing

### 2. Enable APIs
- Search for "Cloud Translation API" and enable
- Search for "Text-to-Speech API" and enable

### 3. Create Service Account
- Go to "Service Accounts"
- Create new service account
- Grant "Editor" role
- Create and download JSON key

### 4. Set Environment Variable

**Windows (Command Prompt)**:
```bash
set GOOGLE_APPLICATION_CREDENTIALS=C:\path\to\your\key.json
python app.py
```

**Windows (PowerShell)**:
```powershell
$env:GOOGLE_APPLICATION_CREDENTIALS = "C:\path\to\your\key.json"
python app.py
```

**macOS/Linux**:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/key.json"
python app.py
```

## 💻 Usage Guide

### 1. Translate Text
- Type or paste English text
- Click **Translate** button
- Kannada translation appears below

### 2. Hear Pronunciation
- Click **Speak** button after translation
- Audio plays in browser

### 3. Use Voice Input
- Click **Start Listening**
- Speak English clearly
- Click **Stop Listening**
- Transcribed text auto-fills input box

### 4. Copy Translation
- Click **Copy** button
- Text copied to clipboard

## ⚙️ Configuration

### Backend Configuration

Create `.env` file in backend folder:

```env
# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True

# Server Configuration
BACKEND_PORT=5000
API_HOST=localhost
API_PORT=5000
```

### Frontend Configuration

Edit `API_BASE_URL` in `frontend/script.js`:

```javascript
const API_BASE_URL = 'http://localhost:5000';  // Change if backend on different host
```

## 🔧 Troubleshooting

### Backend Connection Error
**Error**: "Cannot connect to server"

**Solution**:
```bash
# Make sure backend is running
cd backend
venv\Scripts\activate  # Windows
python app.py
```

### Speech Recognition Not Working
**Error**: Microphone not detected / Permission denied

**Solution**:
1. Check browser microphone permissions
2. Allow microphone when browser asks
3. Use Chrome or Edge (best support)
4. Reload page

### Google Cloud API Error
**Error**: 401 Unauthorized / API not enabled

**Solution**:
1. Verify service account key path
2. Ensure APIs are enabled in Cloud Console
3. Check service account has correct permissions

### CORS Error
**Error**: "Access to XMLHttpRequest blocked by CORS"

**Solution**:
- Backend already has CORS enabled
- Make sure frontend and backend are on different ports
- Use Python HTTP server for frontend

### No Audio in Text-to-Speech
**Error**: TTS endpoint returns 503

**Solution**:
1. Check Google Cloud credentials are set
2. Verify Text-to-Speech API is enabled
3. Check service account permissions

## 📋 Fallback Mode

The app includes a fallback translation dictionary for common phrases:
- "hello" → "ನಮಸ್ಕಾರ"
- "thank you" → "ಧನ್ಯವಾದ"
- "good morning" → "ಶುಭೋದಯ"
- And more...

Works without Google Cloud, but limited to predefined phrases.

## 🌍 Browser Compatibility

| Browser | Support | Notes |
|---------|---------|-------|
| Chrome | ✅ Full | Best for speech recognition |
| Firefox | ✅ Full | All features working |
| Safari | ✅ Full | All features working |
| Edge | ✅ Full | Best for Windows |
| Opera | ✅ Full | All features working |
| IE 11 | ❌ No | Not supported |

## 📦 Dependencies

### Backend
- **Flask** (2.3.0): Web framework
- **Flask-CORS** (4.0.0): Cross-origin support
- **google-cloud-translate** (3.11.0): Translation API
- **google-cloud-texttospeech** (2.13.0): TTS API
- **requests** (2.31.0): HTTP library
- **python-dotenv** (1.0.0): Environment management

### Frontend
- HTML5 (Web Speech API)
- CSS3 (Modern styling)
- JavaScript (Vanilla, no frameworks)

## 🚀 Deployment

### Deploy Backend to Heroku

1. Create `Procfile`:
```
web: python app.py
```

2. Initialize git and deploy:
```bash
git init
git add .
git commit -m "Initial commit"
heroku create your-app-name
git push heroku main
```

### Deploy Frontend to GitHub Pages

1. Push frontend to GitHub
2. Enable GitHub Pages in repository settings
3. Select main branch as source

### Deploy to AWS/Azure

Refer to their respective documentation for Flask deployment.

## 🔐 Security

- API uses CORS to allow cross-origin requests
- No authentication required for demo
- For production, add user authentication
- Keep Google Cloud credentials private
- Use HTTPS in production

## 📈 Performance

- Translations cached for repeated requests
- Audio compressed to MP3 format
- Frontend minified and optimized
- Backend uses efficient Google APIs

## 🎓 Learning Resources

- Flask: https://flask.palletsprojects.com
- Google Cloud APIs: https://cloud.google.com/docs
- Web Speech API: https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API
- REST API: https://restfulapi.net

## 🐛 Known Issues

- Large text translations may take longer (< 5 seconds)
- Speech recognition works best in quiet environments
- TTS quality depends on Google Cloud voices available

## 📞 Support

For help:
1. Check **Troubleshooting** section
2. Review **API Endpoints** documentation
3. Check browser console for errors (F12)
4. Open an issue on GitHub

## 📝 License

MIT License - Free for personal and commercial use

## 🙏 Credits

Built with:
- Flask framework
- Google Cloud APIs
- Web Speech API
- Modern web technologies

---

**Version**: 1.0.0
**Last Updated**: January 29, 2026
**Author**: Sharath
