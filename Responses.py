import string
import datetime

def responses(input_text):
    user_message = str(input_text).lower().translate(str.maketrans('', '', string.punctuation))

    if user_message in ('hello', 'hi', 'hello there'):
        return "General Kenobi!"

    if user_message.translate(str.maketrans('', '', string.punctuation)) in ('who are you'):
        return "I'm just a happy camper! Rockin' rollin'!"

    if user_message.translate(str.maketrans('', '', string.punctuation)) in ('time'):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "What?"
