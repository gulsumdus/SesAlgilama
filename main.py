# Tüm modülleri bir araya getirerek programı çalıştıran ana dosya.
# *********************************************************************
import json
from face_recognition import wait_for_face
from stt import recognize_speech
from tts import speak_text
from qa_handler import load_qa_data, find_best_answer, save_to_json
from config import EXIT_COMMANDS

LOG_FILE = "conversation_log.json"  # Konuşma geçmişi dosyası

if __name__ == "__main__":
    if wait_for_face():  # Yüz algılandığında başlasın
        speak_text("Merhaba")  # Sesli "Merhaba" mesajı
        print("\nSorunuzu sesli söyleyin veya çıkış için 'çıkış' deyin.")

        qa_data = load_qa_data()

        while True:
            question = recognize_speech()

            if question:
                if question.lower() in EXIT_COMMANDS:
                    print("Programdan çıkılıyor...")
                    speak_text("Görüşmek üzere!")
                    break

                answer = find_best_answer(question, qa_data)
                print(f"Cevap: {answer}")
                speak_text(answer)

                # Konuşmayı JSON dosyasına kaydet
                log_entry = {"question": question, "answer": answer}
                save_to_json(log_entry)

