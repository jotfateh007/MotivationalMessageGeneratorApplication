# 💬 Motivational Message Generator

A Python-based **microservices application** that generates and delivers personalized motivational messages using AI, email, and voice narration.  
Each service runs independently and communicates through shared text files that act as simple pipelines.  
**Note:** Each microservice must be executed separately — they run as individual processes that communicate through these shared files rather than through a single main program.

---

## ⚙️ Overview

This project is built using multiple Python microservices that work together to:
- Generate motivational text (AI or prewritten)
- Speak it aloud using Google Text-to-Speech
- Send it to users via Gmail
- Play background music
- Store user preferences and accounts locally

Each service operates independently — meaning you can start, stop, or replace them without affecting the others.  
The main program (`main.py`) coordinates the workflow by reading and writing to communication text files that act as lightweight message queues.

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

## 🧠 How It Works

1. Each microservice runs independently (you can open them in separate terminals or processes).  
2. Services communicate by reading/writing text files — for example, the AI generator writes a message to `AI.txt`, and the narration service reads from it.  
3. `main.py` acts as the coordinator that connects everything together.  

This architecture allows modular development — you can modify or upgrade one microservice without changing the others.

---

## 🛠 Setup Instructions

1. **Install Python 3**  
   Ensure Python 3.x is installed and available in PATH.

2. **Install Dependencies**  

3. **Run Microservices**  
   Launch each service separately in different terminals:
   ```
   python main.py
   python artificialIntelligence.py
   python voiceNarration.py
   python sendEmail.py
   python playMusic.py
   python microservice_A.py
   ```

   (Each process will continuously read and write to its corresponding `.txt` file.)

---

## 🧩 Technologies  
Python · gTTS · OpenRouter (Gemini) · SMTP · pygame  

---

## 🎯 Purpose  
To demonstrate a modular, microservice-based approach to AI-driven personalization — combining motivational message generation, voice narration, and delivery across independent components.
