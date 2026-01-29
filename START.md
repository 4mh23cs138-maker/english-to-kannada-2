# 🚀 STARTUP INSTRUCTIONS

## Welcome to English to Kannada Translator!

This document will guide you through starting the application.

---

## ⚡ FASTEST START (Recommended for First Run)

### What You Need
- Python 3.8 or higher
- A modern web browser

### Step 1: Open PowerShell/Command Prompt
```powershell
# Navigate to the project folder
cd C:\Users\STUDENT\Desktop\sharath\english-to-kannada-2
```

### Step 2: Run Windows Setup Script
```powershell
.\setup.bat
```

This will automatically:
- Create Python virtual environment
- Install dependencies
- Show you next steps

### Step 3: Start Backend (in Terminal 1)
```powershell
cd backend
venv\Scripts\activate
python app_simple.py
```

You should see:
```
Running on http://127.0.0.1:5000
```

### Step 4: Start Frontend (in Terminal 2)
```powershell
cd frontend
python -m http.server 8000
```

You should see:
```
Serving HTTP on 0.0.0.0 port 8000
```

### Step 5: Open in Browser
```
http://localhost:8000
```

✅ **You're done! The app is running!**

---

## 📖 DETAILED SETUP

### For Windows Users

**Terminal 1 - Backend Setup & Run**:
```powershell
# Navigate to project
cd C:\Users\STUDENT\Desktop\sharath\english-to-kannada-2

# Go to backend folder
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install Flask and Flask-CORS only
pip install Flask Flask-CORS

# Run the simple translator (no Google Cloud needed)
python app_simple.py
```

**Terminal 2 - Frontend Setup & Run**:
```powershell
# In new terminal/PowerShell
cd C:\Users\STUDENT\Desktop\sharath\english-to-kannada-2\frontend

# Start web server
python -m http.server 8000
```

**Then in Browser**:
```
Visit: http://localhost:8000
```

### For macOS/Linux Users

**Terminal 1 - Backend Setup & Run**:
```bash
# Navigate to project
cd ~/Desktop/sharath/english-to-kannada-2

# Go to backend folder
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install Flask and Flask-CORS
pip install Flask Flask-CORS

# Run the simple translator
python app_simple.py
```

**Terminal 2 - Frontend Setup & Run**:
```bash
# In new terminal
cd ~/Desktop/sharath/english-to-kannada-2/frontend

# Start web server
python -m http.server 8000
```

**Then in Browser**:
```
Visit: http://localhost:8000
```

---

## 🎮 Using the Application

### Translate Text
1. Type English text in the left box
2. Click **"Translate"** button
3. Kannada translation appears in the right box

### Listen to Pronunciation
1. After translating, click **"Speak"** button
2. Listen to Kannada audio pronunciation

### Use Voice Input
1. Click **"Start Listening"** button
2. Speak English clearly into your microphone
3. Click **"Stop Listening"**
4. Your speech is transcribed into the input box

### Copy Translation
1. Click **"Copy"** button
2. Kannada text is copied to your clipboard

---

## 🔧 Two Versions Available

### Version 1: Simple (No Google Cloud Needed)
**File**: `backend/app_simple.py`
- **Best for**: Testing, learning, quick start
- **Translations**: ~50 common phrases
- **TTS**: Not available
- **Setup time**: < 2 minutes

```bash
python app_simple.py
```

### Version 2: Full Features (Google Cloud Required)
**File**: `backend/app.py`
- **Best for**: Production, unlimited translations
- **Translations**: Any English text
- **TTS**: Full Kannada speech synthesis
- **Setup time**: ~15 minutes (includes Google Cloud setup)

```bash
set GOOGLE_APPLICATION_CREDENTIALS=C:\path\to\key.json
python app.py
```

---

## ✅ Checklist Before Starting

- [ ] Python 3.8+ installed (check with `python --version`)
- [ ] In the project root directory
- [ ] Two terminal windows open (for backend and frontend)
- [ ] Microphone connected (for speech recognition)
- [ ] Speaker working (for listening to pronunciation)

---

## 🆘 Common Issues & Solutions

### Issue: "Python is not recognized"
**Solution**: Python not installed or not in PATH
```
1. Install Python from https://www.python.org/downloads/
2. Make sure "Add Python to PATH" is checked during installation
3. Restart terminal after installation
```

### Issue: Port 5000 already in use
**Solution**: Change port in app.py
```
Find: app.run(debug=True, host='0.0.0.0', port=5000)
Change to: app.run(debug=True, host='0.0.0.0', port=5001)
Update frontend script.js: const API_BASE_URL = 'http://localhost:5001'
```

### Issue: Port 8000 already in use
**Solution**: Use a different port
```powershell
python -m http.server 9000
# Then visit http://localhost:9000
```

### Issue: "Cannot connect to server"
**Solution**:
1. Make sure backend terminal shows "Running on http://127.0.0.1:5000"
2. Check that both terminals are running
3. Ensure port 5000 and 8000 are not blocked by firewall

### Issue: Microphone not working
**Solution**:
1. Check browser microphone permissions (click lock icon in address bar)
2. Allow microphone access when browser asks
3. Use Chrome or Edge for best support
4. Restart browser

### Issue: No sound from "Speak" button
**Solution**:
1. Check speaker volume
2. Make sure browser hasn't muted audio
3. Simple version (app_simple.py) doesn't have TTS
4. Use full version (app.py) with Google Cloud for speech

---

## 📊 What's Running?

When both terminals are running, you have:

```
Backend (Python Flask Server)
├── Port: 5000
├── Translates English to Kannada
└── Generates speech audio

Frontend (Web Application)
├── Port: 8000
├── User interface in browser
└── Captures voice input
```

---

## 🎯 Next Steps After Starting

1. **Test Translation**: Type "hello" and click Translate
2. **Test Voice**: Click "Start Listening" and say "thank you"
3. **Check Results**: Verify translated text appears
4. **Explore**: Try different phrases and features

---

## 🔌 Important Endpoints

When running:
- Backend API: `http://localhost:5000`
- Frontend UI: `http://localhost:8000`
- Health check: `http://localhost:5000/health`

---

## 🚫 Stopping the Application

**To stop backend**: In backend terminal, press `Ctrl + C`
**To stop frontend**: In frontend terminal, press `Ctrl + C`

---

## 📚 Documentation

- **QUICKSTART.md** - 3-minute quick start
- **SETUP.md** - Detailed setup instructions
- **PROJECT_SUMMARY.md** - Project overview and features

---

## 💡 Tips

1. **Keep terminals open**: Don't close backend or frontend terminal while using
2. **Modern browser**: Use Chrome, Firefox, Safari, or Edge
3. **Quiet environment**: Better speech recognition in quiet places
4. **Clear speech**: Speak clearly for best transcription
5. **Test first**: Try "hello" before complex sentences

---

## 🎓 Learning

The project demonstrates:
- Python Flask web framework
- REST APIs (GET, POST)
- Frontend JavaScript
- HTML5 Web Speech API
- Google Cloud APIs
- CORS and API communication

---

## 🎉 Ready to Start?

Follow the **FASTEST START** section above and enjoy translating!

If you have any questions, check the troubleshooting section or refer to the detailed documentation files.

**Happy translating! 🌍**

---

**Last Updated**: January 29, 2026
**Version**: 1.0.0
