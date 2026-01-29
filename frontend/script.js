// Configuration
const API_BASE_URL = 'http://localhost:5000';

// DOM Elements
const englishInput = document.getElementById('englishInput');
const kannadaOutput = document.getElementById('kannadaOutput');
const translateBtn = document.getElementById('translateBtn');
const clearBtn = document.getElementById('clearBtn');
const copyBtn = document.getElementById('copyBtn');
const speakBtn = document.getElementById('speakBtn');
const startListenBtn = document.getElementById('startListenBtn');
const stopListenBtn = document.getElementById('stopListenBtn');
const speechStatus = document.getElementById('speechStatus');
const loadingIndicator = document.getElementById('loadingIndicator');
const messageContainer = document.getElementById('messageContainer');
const audioPlayer = document.getElementById('audioPlayer');

// Speech Recognition Setup
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();
recognition.lang = 'en-US';
recognition.continuous = false;
recognition.interimResults = true;

// Event Listeners
translateBtn.addEventListener('click', handleTranslate);
clearBtn.addEventListener('click', handleClear);
copyBtn.addEventListener('click', handleCopy);
speakBtn.addEventListener('click', handleSpeak);
startListenBtn.addEventListener('click', handleStartListening);
stopListenBtn.addEventListener('click', handleStopListening);

// Speech Recognition Events
recognition.onstart = () => {
    startListenBtn.disabled = true;
    stopListenBtn.disabled = false;
    speechStatus.textContent = '🎤 Listening...';
    speechStatus.classList.add('active');
};

recognition.onresult = (event) => {
    let interimTranscript = '';
    
    for (let i = event.resultIndex; i < event.results.length; i++) {
        const transcript = event.results[i][0].transcript;
        
        if (event.results[i].isFinal) {
            englishInput.value += transcript + ' ';
        } else {
            interimTranscript += transcript;
        }
    }
    
    if (interimTranscript) {
        speechStatus.textContent = `📝 ${interimTranscript}`;
    }
};

recognition.onerror = (event) => {
    showMessage(`Error: ${event.error}`, 'error');
    speechStatus.textContent = `❌ Error: ${event.error}`;
    startListenBtn.disabled = false;
    stopListenBtn.disabled = true;
};

recognition.onend = () => {
    startListenBtn.disabled = false;
    stopListenBtn.disabled = true;
    speechStatus.textContent = '✓ Done listening';
    speechStatus.classList.remove('active');
    setTimeout(() => {
        speechStatus.textContent = '';
        speechStatus.classList.remove('active');
    }, 2000);
};

// Translation Handler
async function handleTranslate() {
    const text = englishInput.value.trim();
    
    if (!text) {
        showMessage('Please enter English text', 'error');
        return;
    }
    
    showLoading(true);
    
    try {
        const response = await fetch(`${API_BASE_URL}/translate`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        
        if (data.success) {
            kannadaOutput.value = data.kannada;
            showMessage('✓ Translation successful!', 'success');
        } else {
            showMessage(`Error: ${data.error}`, 'error');
        }
    } catch (error) {
        showMessage(`Translation failed: ${error.message}`, 'error');
        console.error('Translation error:', error);
    } finally {
        showLoading(false);
    }
}

// Clear Handler
function handleClear() {
    englishInput.value = '';
    kannadaOutput.value = '';
    showMessage('Cleared!', 'success');
}

// Copy Handler
function handleCopy() {
    const text = kannadaOutput.value;
    
    if (!text) {
        showMessage('Nothing to copy', 'error');
        return;
    }
    
    navigator.clipboard.writeText(text).then(() => {
        showMessage('✓ Copied to clipboard!', 'success');
    }).catch(err => {
        showMessage('Failed to copy', 'error');
        console.error('Copy error:', err);
    });
}

// Text-to-Speech Handler
async function handleSpeak() {
    const text = kannadaOutput.value.trim();
    
    if (!text) {
        showMessage('Please translate text first', 'error');
        return;
    }
    
    showLoading(true);
    
    try {
        const response = await fetch(`${API_BASE_URL}/text-to-speech`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        
        if (data.success) {
            // Play audio from base64
            const audioSource = `data:${data.mime_type};base64,${data.audio}`;
            audioPlayer.src = audioSource;
            audioPlayer.play();
            showMessage('🔊 Playing audio...', 'info');
        } else {
            showMessage(`Error: ${data.error}`, 'error');
        }
    } catch (error) {
        showMessage(`Text-to-speech failed: ${error.message}`, 'error');
        console.error('TTS error:', error);
    } finally {
        showLoading(false);
    }
}

// Speech Recognition Handlers
function handleStartListening() {
    englishInput.focus();
    recognition.start();
}

function handleStopListening() {
    recognition.stop();
}

// Utility Functions
function showMessage(message, type = 'info') {
    const messageEl = document.createElement('div');
    messageEl.className = `message ${type}`;
    messageEl.innerHTML = `
        <span>${message}</span>
        <button class="message-close" onclick="this.parentElement.remove()">×</button>
    `;
    
    messageContainer.appendChild(messageEl);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        if (messageEl.parentElement) {
            messageEl.remove();
        }
    }, 5000);
}

function showLoading(isLoading) {
    loadingIndicator.style.display = isLoading ? 'block' : 'none';
}

// Check API connectivity on load
window.addEventListener('load', () => {
    checkAPIConnectivity();
    
    // Add Enter key support for translation
    englishInput.addEventListener('keydown', (e) => {
        if (e.ctrlKey && e.key === 'Enter') {
            handleTranslate();
        }
    });
});

async function checkAPIConnectivity() {
    try {
        const response = await fetch(`${API_BASE_URL}/health`);
        if (response.ok) {
            showMessage('✓ Connected to server', 'success');
        } else {
            showMessage('⚠️ Server connection issue', 'error');
        }
    } catch (error) {
        showMessage('❌ Cannot connect to server. Make sure backend is running on port 5000', 'error');
        console.error('API connectivity error:', error);
    }
}
