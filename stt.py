#Konuşma tanıma (Speech-to-Text) işlemlerini içerir.
#**************************************************************************

import speech_recognition as sr  # Import speech recognition library

def recognize_speech():
    recognizer = sr.Recognizer()  # Initialize speech recognizer
    with sr.Microphone() as source:  # Use microphone as input
        print("Bir şeyler söyleyin...")  # Prompt user to speak
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        audio = recognizer.listen(source)  # Capture audio

    try:
        text = recognizer.recognize_google(audio, language="tr-TR")  # Convert speech to text
        print(f"Tanınan metin: {text}")  # Print recognized text
        return text
    except sr.UnknownValueError:  # Handle case when speech is unclear
        print("Ses anlaşılamadı. Lütfen tekrar deneyin.")
        return None
    except sr.RequestError:  # Handle internet issues
        print("STT servisine erişilemedi. İnternet bağlantınızı kontrol edin.")
        return None
