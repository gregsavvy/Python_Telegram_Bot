import string
import datetime

def responses(input_text):
    user_message = str(input_text).lower().translate(str.maketrans('', '', string.punctuation))

    for msg in user_message.split():

        if user_message in ('hello', 'hi', 'hello there'):
            return "General Kenobi!"

        if user_message in ('who are you'):
            return "I'm just a happy camper! Rockin' rollin'!"

        if user_message in ('are you free'):
            return "It’s only after we’ve lost everything that we’re free to do anything."

        if msg in ('try'):
            return "Do, or do not. There is no “‘try'”."

        if msg in ('love'):
            return "Sometimes I wish I had never met you. Because then I could go to sleep at night not knowing there was someone like you out there."

        if msg in ('strange'):
            return "I believe whatever doesn’t kill you, simply makes you…stranger."

        if msg in ('bye', 'goodbye'):
            return "I'll be back."

        if msg in ('freedom'):
            return "They may take our lives, but they will never take… our FREEDOM!"

        if msg in ('complicated'):
            return "My momma always said, “Life is like a box of chocolates, you never know what you’re gonna get."

        if msg in ('motivation', 'sad'):
            return "Don’t ever let somebody tell you you can’t do something, not even me. Alright? You dream, you gotta protect it. People can’t do something themselves, they wanna tell you you can’t do it. If you want something, go get it. Period."

        if msg in ('life'):
            return "What we do in life echoes in eternity."

        if msg in ('funny'):
            return "It's just a flesh wound."

        if user_message in ('time'):
            now = datetime.now()
            date_time = now.strftime("%d/%m/%y, %H:%M:%S")

            return str(date_time)

    return "What?"
