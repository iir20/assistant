from gtts import gTTS
import os

class VoiceEngine:
    def speak(self, text):
        tts = gTTS(text=text, lang='en')
        tts.save("response.mp3")
        os.system("mpg321 response.mp3")