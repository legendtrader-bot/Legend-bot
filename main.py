import telebot, re
BOT_TOKEN = "8915149038:AAFSIV4p_49ubqMHBwc7xi1UCeWNUaToDgQ"
bot = telebot.TeleBot(BOT_TOKEN)
MY_LINK = "https://qxbroker.com/en/sign-up/?lid=2372198"
DEPOSIT_DONE = {"93723332": 40}

@bot.message_handler(func=lambda m: True)
def check(m):
    f = re.findall(r'\d{6,10}', m.text)
    if not f: return
    tid = f[0]
    dep = DEPOSIT_DONE.get(tid, 0)
    if dep >= 20:
        msg = f"✅ ID VERIFIED: {tid}\n💰 Deposit: ${dep} - DONE"
    else:
        msg = f"✅ ID VERIFIED: {tid}\n🔗 Mere link se bani hai - CONFIRM\n💰 Deposit: ${dep}\n⚠️ Status: Deposit pending - $20 deposit karo\n👇 Link: {MY_LINK}\nVerified but 20$ deposit ni ha"
    bot.reply_to(m, msg)
bot.infinity_polling()
