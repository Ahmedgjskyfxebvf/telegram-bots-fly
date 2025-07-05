import telebot

TOKEN = '7863983745:AAFJrRYMwgSIJb7ZXQuuWTjdMzTw7XpGpVk'
bot = telebot.TeleBot(TOKEN)

# تخزين حالات المستخدمين الذين في انتظار كلمة السر
waiting_for_password = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    waiting_for_password[user_id] = True
    bot.send_message(user_id, "🔒 أدخل كلمة السر للمتابعة:")

@bot.message_handler(func=lambda message: True)
def handle_password(message):
    user_id = message.from_user.id
    if waiting_for_password.get(user_id):
        if message.text.strip() == "15041978":
            bot.send_message(user_id, "مرحبًا سيدي أحمد ✅")
        else:
            bot.send_message(user_id, "❌ كلمة السر غير صحيحة")
        waiting_for_password.pop(user_id, None)  # إزالة الحالة بعد الرد
    else:
        bot.send_message(user_id, "اضغط /start لبدء الاستخدام.")

# تشغيل البوت
print("🤖 البوت يعمل الآن...")
bot.infinity_polling()