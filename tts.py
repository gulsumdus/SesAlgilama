import os
import json
import time
from gtts import gTTS
import playsound
from config import AUDIO_FOLDER, LOG_FILE


# Klasör yoksa oluştur
os.makedirs(AUDIO_FOLDER, exist_ok=True)

def speak_text(text):
    try:
        # Benzersiz bir ses dosyası oluştur
        timestamp = int(time.time())  # Unix zaman damgası
        file_path = os.path.join(AUDIO_FOLDER, f"response_{timestamp}.mp3")
        
        # Metni sese çevir ve kaydet
        tts = gTTS(text=text, lang="tr")
        tts.save(file_path)

        # JSON'a konuşmayı kaydet
        log_entry = {"timestamp": timestamp, "text": text, "audio_file": file_path}
        save_to_json(log_entry)

        # Ses dosyasını çal
        playsound.playsound(file_path)

    except Exception as e:
        print(f"Sesli yanıt sırasında bir hata oluştu: {e}")

def save_to_json(log_entry):
    """Konuşmayı JSON formatında saklar."""
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)

    with open(LOG_FILE, "r+", encoding="utf-8") as file:
        data = json.load(file)
        data.append(log_entry)  # Yeni konuşmayı ekle
        file.seek(0)
        json.dump(data, file, ensure_ascii=False, indent=4)

# Test
if __name__ == "__main__":
    speak_text("Merhaba, nasılsınız?")

