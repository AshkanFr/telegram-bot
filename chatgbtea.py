

# import telebot
# import requests


# TELEGRAM_TOKEN = "7961077915:AAHUALRpnmSjimTM8PC4HTCoYgDgKxkN7rY"
# OPENROUTER_API_KEY = "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"


# bot = telebot.TeleBot(TELEGRAM_TOKEN)


# OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"


# def get_openrouter_response(prompt):
#     headers = {
#         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "model": "mistralai/mistral-7b-instruct", 
#         "messages": [{"role": "user", "content": prompt}],
#         "max_tokens": 100
#     }
#     response = requests.post(OPENROUTER_API_URL, headers=headers, json=data)

#     if response.status_code == 200:
#         return response.json()["choices"][0]["message"]["content"].strip()
#     else:
#         return "Somthing went wrong :("


# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     user_input = message.text
#     processing_message = bot.reply_to(message, "Wait please ...")

#     response = get_openrouter_response(user_input)

#     bot.delete_message(chat_id=message.chat.id, message_id=processing_message.message_id)
#     bot.reply_to(message, response)

# bot.polling()




#--------------------------------------------------------------------------------------------------------------------#

#Chatgpt API

import telebot # type: ignore
import requests # type: ignore

TELEGRAM_TOKEN = "7961077915:AAHUALRpnmSjimTM8PC4HTCoYgDgKxkN7rY"
OPENROUTER_API_KEY = "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"
bot = telebot.TeleBot(TELEGRAM_TOKEN)
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

def get_openrouter_response(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-4-turbo",  
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 200
    }
    response = requests.post(OPENROUTER_API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        return f"Somthing went wrong :( {response.json()}"

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    processing_message = bot.reply_to(message, "Please wait ...")

    response = get_openrouter_response(user_input)

    bot.delete_message(chat_id=message.chat.id, message_id=processing_message.message_id)
    bot.reply_to(message, response)

bot.polling()







