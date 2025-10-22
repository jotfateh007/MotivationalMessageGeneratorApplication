import io
import pygame
from gtts import gTTS
from translate import Translator
import preferences


def speak(text, language):
    translator = Translator(to_lang=language)
    translation = translator.translate(text)

    tts = gTTS(text=translation, lang=language)

    audio_stream = io.BytesIO()
    tts.write_to_fp(audio_stream)
    audio_stream.seek(0)
    pygame.mixer.init()

    sound = pygame.mixer.Sound(audio_stream)
    sound.play()

    while pygame.mixer.get_busy():
        pygame.time.Clock().tick(10)


def isPlaying():
    return pygame.mixer.get_busy()

while True:
    with open("narrate.txt", 'r+') as file:
        message = file.readline().strip()
        if message == "translate":
            username = file.readline().strip()
            messageToSpeak = file.read()
            file.seek(0)
            file.truncate(0)
            prefs = preferences.get_user_preferences(username)
            language = prefs['language']
            speak(messageToSpeak, language)
            if not isPlaying():
                file.write('done')


