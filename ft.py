import requests,telebot
from telebot import types
# تم البرمجة بواسطة ايجوس
ti=0
token = input("5444765773:AAH5nXSu4vi07ZpLodhYwpECUBk2nagCgZQ") #توكن بوتك
print('- اذهب للبوت واضغط \n /start')
bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['start'])
def Start(message):
    id = message.from_user.id
    a = message.from_user.first_name
    b = message.from_user.username
    channel = "PatroenDev" #قناتك
    x = requests.get(f"https://api.telegram.org/bot{token}/getChatMember?chat_id=@{channel}&user_id={id}").text
    if x.count("left") or x.count("Bad Request: user not found"):
        z = types.InlineKeyboardMarkup()
        x = types.InlineKeyboardButton(text = "اضـغط هنا ",url=f"t.me/{channel}")
        z.add(x)
        return bot.send_message(message.chat.id,f'''<strong>Botu Kullanmak İçin Kanala Abone Olun !
-  القناة :- @{Patroenss_bot} .
- بعد الاشتراك في القناة ارسل : /start </strong>''',reply_markup=z,parse_mode='html')
    bot.reply_to(message, """  
*
اهلا بك {}
تم اشتراكك بالقناة
your user : {}
your id : {}
*
""".format(a,b,id) , parse_mode = "markdown" , reply_markup = A)
A = types.InlineKeyboardMarkup(row_width=2)
F = types.InlineKeyboardButton(text="devloper",url='https://t.me/PatroenDev')
A.add(F)
bot.polling()