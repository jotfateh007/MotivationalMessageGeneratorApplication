# 💬 Motivational Message Generator

A Python-based **microservices application** that generates and delivers personalized motivational messages using AI, email, and voice narration.  
Each service runs independently and communicates through shared text files that act as simple pipelines.

---

## ⚙️ Overview

This project is built using multiple Python microservices that work together to:
- Generate motivational text (AI or prewritten)
- Speak it aloud using Google Text-to-Speech
- Send it to users via Gmail
- Play background music
- Store user preferences and accounts locally

---

## 🧩 Architecture

| File | Description |
|------|--------------|
| `main.py` | Central orchestrator; manages the UI, menu, and inter-service communication. |
| `artificialIntelligence.py` | Generates motivational messages using OpenRouter (Gemini). |
| `voiceNarration.py` | Narrates messages using Google Text-to-Speech (gTTS) and `pygame`. |
| `sendEmail.py` | Sends motivational messages to users via Gmail SMTP. |
| `playMusic.py` | Handles background music playback and user controls. |
| `microservice_A.py` | Provides random motivational quotes from local text files. |
| `preferences.py` | Stores and retrieves user preferences (language, narration, etc.). |
| `accountCreation.py` / `login.py` | Manage user accounts and authentication. |

---

## 📁 Communication Files (Pipelines)

These `.txt` files act as message queues between services:

| File | Purpose |
|------|----------|
| `AI.txt` | Main ↔ AI generator communication. |
| `narrate.txt` | Main ↔ Narration service. |
| `music.txt` | Main ↔ Music player. |
| `messageGen.txt` | Main ↔ Static quote generator. |

Persistent data:
- `users.json` → user credentials  
- `user_preferences.json` → language & narration settings  
- `api.txt` → your OpenRouter API key  

---

## 🛠 Setup Instructions

1. **Install Python 3**  
   Ensure Python 3.x is installed and available in PATH.

2. **Install Dependencies**
