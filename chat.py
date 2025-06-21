from groq_api import send_message

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

        # Yeni kullanıcı mesajını geçmişe ekle
        chat_history.append({"role": "user", "content": user_input})

        # API'den yanıt al
        reply = send_message(chat_history)

        # Model cevabını geçmişe ekle
        chat_history.append({"role": "assistant", "content": reply})

        print(f"🤖 Bot: {reply}\n")

if __name__ == "__main__":
    main()
