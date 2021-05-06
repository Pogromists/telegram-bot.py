import telebot;
bot = telebot.TeleBot('1629776304:AAFoAoCCBwLohWbMzYEb-SRos2nNx-_fcx0');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "Привет": bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.") ;
  elif message.text == "/help": bot.send_message(message.from_user.id, "Напиши Привет");
