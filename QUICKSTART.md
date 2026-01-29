# 🚀 QUICK START GUIDE

## Start in 3 Steps!

### Option 1: Without Google Cloud (Recommended for Testing)

**Step 1: Terminal 1 - Start Backend**
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install Flask Flask-CORS
python app_simple.py
```

**Step 2: Terminal 2 - Start Frontend**
```bash
cd frontend
python -m http.server 8000
```

**Step 3: Open Browser**
```
http://localhost:8000
```

✅ Done! The app is running!

---

### Option 2: With Google Cloud (Full Features)

**Step 1: Google Cloud Setup**
- Create project at https://console.cloud.google.com
- Enable "Cloud Translation API" and "Text-to-Speech API"
- Create service account and download JSON key
- Set environment variable (Windows):
```bash
set GOOGLE_APPLICATION_CREDENTIALS=path\to\key.json
```

**Step 2: Terminal 1 - Start Backend**
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

**Step 3: Terminal 2 - Start Frontend**
```bash
cd frontend
python -m http.server 8000
```

**Step 4: Open Browser**
```
http://localhost:8000
```

✅ Full features enabled!

---

## 💡 What You Can Do

1. **Type English** → Gets translated to Kannada
2. **Click Speak** → Hear Kannada pronunciation
3. **Click Start Listening** → Speak English into microphone
4. **Click Copy** → Copy Kannada text to clipboard

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| Port 5000 already in use | Change `port=5000` to `port=5001` in app.py |
| Python not found | Install from python.org or use python3 command |
| Port 8000 already in use | Use `python -m http.server 9000` instead |
| Microphone not working | Allow microphone permission in browser |

---

## 📁 File Structure

```
project/
├── backend/
│   ├── app.py (Google Cloud version)
│   ├── app_simple.py (Simple fallback version)
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
└── QUICKSTART.md (this file)
```

---

## 🎯 Using app_simple.py

Use this if you don't have Google Cloud setup:

- Works offline (mostly)
- Uses dictionary for translations
- No API costs
- Limited to predefined phrases
- No text-to-speech (comment out TTS button)

---

## 📦 Requirements

- Python 3.8+
- Browser (Chrome, Firefox, Safari, Edge)
- Optional: Google Cloud account

---

## 🔗 Important Ports

- Backend: http://localhost:5000
- Frontend: http://localhost:8000

Keep them different to avoid conflicts!

---

## 📞 Need Help?

1. Check SETUP.md for detailed instructions
2. Check terminal output for error messages
3. Open browser Developer Tools (F12) to see errors
4. Ensure both backend and frontend are running

---

**Good luck! Happy translating! 🎉**
