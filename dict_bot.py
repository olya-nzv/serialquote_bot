from telebot import TeleBot, types

bot = TeleBot(token='my token', parse_mode='html') 

DEFINITOINS = {
    'sopranos': 'Genetic predispositions are only that: predispositions',
    'friends': 'Joey does not share food!',
    'how i met your mother': 'whenever im sad, i stop being sad and be awesome instead',
    'daria': 'I do not have low self-esteem. I have low esteem for everyone else',
    'office': 'I am not superstitious, but I am a little stitious',
    'house': 'Everybody lies',
    'simpsons': 'Do h!',
    'charmed': 'Every family has its demons',
    'the big bang theory': 'That is My Spot',
    'scrubs': 'Who is got two thumbs and does not give a crap? Bob Kelso',
    'family guy': 'Lets go drink until we can not feel feelings anymore',
}

@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    bot.send_message(
        chat_id= message.chat.id, 
        text='Hey! Enter the series you like, for example, Friends',
    )

@bot.message_handler()
def message_handler(message: types.Message):
    definition = DEFINITOINS.get(
        message.text.lower(), 
    )
 
    if definition is None:
       
        bot.send_message(
            chat_id=message.chat.id,
            text='Sorry. I have not quoted this series yet',
        )
        return
    
    bot.send_message(
        chat_id=message.chat.id,
        text=f'your quote:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f'come on next',
    )

def main():
    bot.infinity_polling()

if __name__ == '__main__':
    main()
