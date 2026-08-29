from cryptography.fernet import Fernet
import os
import telebot

TOKEN = "8966164743:AAew6MAK0qsq8RCTY3Qy41mHyfZZwugFVEQ"
MY_CHAT_ID = "5539596358"
DB_FILE = "vault.enc"
KEY_FILE = "secret.key"

bot = telebot.TeleBot(TOKEN)


def get_or_create_key():
  if not os.path.exists(KEY_FILE):
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
      key_file.write(key)
  else:
    with open(KEY_FILE, "rb") as key_file:
      key = key_file.read()
  return key


@bot.message_handler(
    func=lambda message: str(message.chat.id) == str(MY_CHAT_ID)
)
def secure_vault(message):
  text = message.text
  key = get_or_create_key()
  cipher = Fernet(key)

  if text.startswith("/save"):
    data_to_save = text.replace("/save", "").strip()
    if not data_to_save:
      bot.reply_to(message, "الرجاء كتابة البيانات بعد الأمر /save")
      return

    encrypted_text = cipher.encrypt(data_to_save.encode("utf-8"))
    with open(DB_FILE, "ab") as f:
      f.write(encrypted_text + b"\n")

    bot.reply_to(message, "تم حفظ البيانات وتشفيرها بنجاح 🔒.")

  elif text == "/get":
    if not os.path.exists(DB_FILE):
      bot.reply_to(message, "لا توجد بيانات محفوظة بعد.")
      return

    try:
      with open(DB_FILE, "rb") as f:
        lines = f.readlines()

      decrypted_data = []
      for line in lines:
        if line.strip():
          decrypted_text = cipher.decrypt(line.strip()).decode("utf-8")
          decrypted_data.append(decrypted_text)

      result = "\n".join(decrypted_data)
      bot.reply_to(message, f"البيانات المحفوظة:\n\n{result}")
    except Exception as e:
      bot.reply_to(message, "حدث خطأ أثناء فك التشفير.")
  else:
    bot.reply_to(
        message,
        "الأوامر المتاحة:\n/save [البيانات] - للحفظ\n/get - لعرض البيانات",
    )


bot.infinity_polling()
