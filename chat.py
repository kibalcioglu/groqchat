from groq_api import send_message
from zemberek_bridge import correct_text

def main():
    print("🤖 GroqChat'e hoş geldiniz! (Çıkmak için 'çık' yazın)\n")

    # İlk system mesajı – modelin kimliğini belirler
    chat_history = [
        {"role": "system", "content": "Sen yalnızca Türkçe konuşan, yardımsever bir sohbet asistanısın. Asla İngilizce konuşma."}
    ]

    while True:
        user_input = input("🟢 Sen: ").strip()

        if user_input.lower() in ["çık", "exit", "quit"]:
            print("🔚 Sohbet sonlandırıldı. Görüşmek üzere!")
            break

        corrected_user = correct_text(user_input)

        # Yeni kullanıcı mesajını geçmişe ekle
        chat_history.append({"role": "user", "content": corrected_user})

        # API'den yanıt al
        reply = send_message(chat_history)
        corrected_reply = correct_text(reply)

        # Model cevabını geçmişe ekle
        chat_history.append({"role": "assistant", "content": corrected_reply})
        print(f"🤖 Bot: {corrected_reply}\n")

if __name__ == "__main__":
    main()
