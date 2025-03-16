#Metinden konuşmaya (Text-to-Speech) işlemlerini içerir.
import os
from gtts import gTTS
import playsound

def speak_text(text):
    try:
        # Sesli yanıtı kaydet
        tts = gTTS(text=text, lang="tr")
        file_path = "response.txt"
        tts.save(file_path)  # mp3 dosyasını kaydet

        # Dosyanın kaydedildiğinden emin olun
        if os.path.exists(file_path):
            print(f"Ses dosyası kaydedildi: {file_path}")
            playsound.playsound(file_path)  # Ses dosyasını çal
        else:
            print("Ses dosyası kaydedilemedi.")

        os.remove(file_path)  # Ses dosyasını sil

    except Exception as e:
        print(f"Sesli yanıt sırasında bir hata oluştu: {e}")

# Test
speak_text("Merhaba, nasılsınız?")

