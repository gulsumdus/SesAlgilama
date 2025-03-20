import os  # Dosya işlemleri için
import json  # JSON veri işlemleri için
from rapidfuzz import process  # En iyi eşleşmeyi bulmak için

QA_FILE = "sorular.json"  # Soru-cevap veritabanı dosyası
LOG_FILE = "conversation_log.json"  # Kullanıcı konuşma kayıtları dosyası

# Eğer soru-cevap veritabanı yoksa, boş bir JSON dosyası oluştur
if not os.path.exists(QA_FILE):
    with open(QA_FILE, "w", encoding="utf-8") as file:
        json.dump({}, file, ensure_ascii=False, indent=4)  # Boş bir sözlük kaydet

# Eğer konuşma kaydı dosyası yoksa, boş bir JSON listesi oluştur
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", encoding="utf-8") as file:
        json.dump([], file, ensure_ascii=False, indent=4)  # Boş bir liste kaydet

def load_qa_data():
    """Soru-cevap veritabanını yükler ve JSON formatında okur."""
    with open(QA_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)  # JSON verisini oku ve sözlüğe çevir
        except json.JSONDecodeError:
            print("Dosya bozuk veya yanlış formatta.")  # JSON bozuksa uyarı ver
            return {}  # Boş bir sözlük döndür

def find_best_answer(question, qa_dict):
    """Kullanıcının sorusuna en iyi cevabı bulan fonksiyon."""
    if not qa_dict:  # Eğer veritabanı boşsa
        return "Üzgünüm, şu anda veritabanım boş."

    questions = list(qa_dict.keys())  # Veritabanındaki tüm soruları listeye çevir
    best_match, score, _ = process.extractOne(question, questions)  # En iyi eşleşmeyi bul
    
    if score > 80:  # Eğer benzerlik skoru %70'ten büyükse
        answer = qa_dict[best_match]  # En iyi eşleşmenin cevabını al
        save_to_json({"question": question, "answer": answer})  # Konuşmayı log'a kaydet
        return answer  # Cevabı döndür
    
    return add_new_question(question, qa_dict)  # Eğer soru bulunamazsa, yeni ekleme sürecine yönlendir

def save_to_json(log_entry):
    """Konuşmaları JSON formatında saklar ve dosya bozuksa sıfırdan başlatır."""
    try:
        # Dosya aç ve içeriği oku
        with open(LOG_FILE, "r+", encoding="utf-8") as file:
            try:
                data = json.load(file)  # JSON verisini yükle
            except json.JSONDecodeError:  
                data = []  # Eğer dosya bozuksa veya boşsa, yeni bir liste oluştur

        # Yeni veriyi ekleyip güncelle
        data.append(log_entry)
        with open(LOG_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)  # Güncellenmiş veriyi kaydet

    except FileNotFoundError:
        # Eğer dosya bulunamazsa, yeni bir dosya oluştur ve veriyi kaydet
        with open(LOG_FILE, "w", encoding="utf-8") as file:
            json.dump([log_entry], file, ensure_ascii=False, indent=4)


def add_new_question(question, qa_dict):
    """Eğer soru veritabanında yoksa, kullanıcıdan yeni bir cevap isteyerek ekler."""
    print(f"'{question}' sorusunun cevabı bulunamadı. Yeni cevap eklemek ister misiniz? (evet/hayır)")
    choice = input().strip().lower()  # Kullanıcıdan yanıt al ve küçük harfe çevir

    if choice == "evet":
        new_answer = input("Lütfen bu soruya bir cevap yazın: ").strip()  # Kullanıcıdan yeni cevap al
        qa_dict[question] = new_answer  # Yeni soru-cevap çiftini sözlüğe ekle

        # Güncellenmiş veriyi JSON dosyasına kaydet
        with open(QA_FILE, "w", encoding="utf-8") as file:
            json.dump(qa_dict, file, ensure_ascii=False, indent=4)  # JSON'a kaydet

        print("Yeni soru ve cevap başarıyla eklendi.")
        return new_answer  # Yeni cevabı döndür
    else:
        return "Bu soruya şu an için bir cevabım yok."  # Kullanıcı eklemek istemezse varsayılan cevap ver


