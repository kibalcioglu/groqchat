from groq_api import send_message
from zemberek_bridge import correct_text

def main():
    print("🤖 GroqChat'e hoş geldiniz! (Çıkmak için 'çık' yazın)\n")

    # İlk system mesajı – modelin kimliğini belirler
    chat_history = [
        {
            "role": "system",
            "content": (
                "Sen Türkçe\u2019yi doğal, akıcı ve samimi bir üslupla konuşan "
                "bir sohbet asistanısın. Sorulara kısa ve sade cümlelerle yanıt "
                "ver, gereksiz resmi ifadelerden kaçın. Emin olmadığın konularda "
                "tahmin yürütme, kısaca 'Bilmiyorum' de. Web sitelerini gezemez "
                "ve gerçek zamanlı içerik göremezsin."
            ),
        }
    ]

    while True:
        user_input = input("🟢 Sen: ").strip()

        if user_input.lower() in ["çık", "exit", "quit"]:
            print("🔚 Sohbet sonlandırıldı. Görüşmek üzere!")
            break

        corrected_user = correct_text(user_input)

        if corrected_user != user_input:
            print(f"\U0001F7E2 Sen: {user_input}")
            print(f"\U0001F7E2 D\u00fczeltilmi\u015f: {corrected_user}")

        # Yeni kullanıcı mesajını geçmişe ekle
        chat_history.append({"role": "user", "content": corrected_user})

        # API'den yanıt al
        reply = send_message(chat_history)
        corrected_reply = correct_text(reply)

        # Model cevabını geçmişe ekle
        chat_history.append({"role": "assistant", "content": corrected_reply})

        if corrected_reply != reply:
            print(f"\U0001F916 Bot: {reply}")
            print(f"\U0001F916 D\u00fczeltilmi\u015f: {corrected_reply}\n")
        else:
            print(f"\U0001F916 Bot: {corrected_reply}\n")

if __name__ == "__main__":
    main()
