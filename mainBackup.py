#Tüm modülleri bir araya getirerek programı çalıştıran ana dosya.
#*********************************************************************
from stt import recognize_speech  # Import speech-to-text function
from tts import speak_text  # Import text-to-speech function
from qa_handler import load_qa_data, find_best_answer  # Import Q&A functions

def main():
    qa_data = load_qa_data()  # Load question-answer data

    while True:
        print("\nSorunuzu sesli söyleyin veya çıkış için 'çıkış' deyin.")
        question = recognize_speech()  # Get user input via speech

        if question:
            if question.lower() in ["çıkış", "kapat", "bitir"]:  # Exit commands
                print("Programdan çıkılıyor...")
                speak_text("Görüşmek üzere!")  # Speak exit message
                break

            answer = find_best_answer(question, qa_data)  # Find the best answer
            print(f"Cevap: {answer}")
            speak_text(answer)  # Speak the answer

if __name__ == "__main__":
    main()  # Run the main function
