#Metinden konuşmaya (Text-to-Speech) işlemlerini içerir.
import os
from gtts import gTTS
#import playsound

def speak_text(text):
    try:
        # Sesli yanıtı kaydet
        tts = gTTS(text=text, lang="tr")
        file_path = "response.mp3"
        tts.save(file_path)  # mp3 dosyasını kaydet

        # # Dosyanın kaydedildiğinden emin olun// bu kısımda hata veriyor !!
        # if os.path.exists(file_path):
        #     print(f"Ses dosyası kaydedildi: {file_path}")
        #     playsound.playsound(file_path)  # Ses dosyasını çal
        # else:
        #     print("Ses dosyası kaydedilemedi.")
        
        os.system(f'start {file_path}')  # Windows'ta varsayılan medya oynatıcı ile çal
        os.remove(file_path)  # Ses dosyasını sil

    except Exception as e:
        print(f"Sesli yanıt sırasında bir hata oluştu: {e}")

# Test
speak_text("Merhaba, nasılsınız?")

