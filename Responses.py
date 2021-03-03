import string
import datetime

def responses(input_text):
    user_message = str(input_text).lower().translate(str.maketrans('', '', string.punctuation))

    for msg in user_message.split():

        if user_message in ('hello', 'hi', 'hello there'):
            return "General Kenobi!"

        if user_message in ('who are you'):
            return "I'm just a happy camper! Rockin' rollin'!"

        if msg in ('try'):
            return "Do, or do not. There is no “‘try'”."

        if msg in ('bye', 'goodbye'):
            return "I'll be back."

        if msg in ('freedom'):
            return "They may take our lives, but they will never take… our FREEDOM!"

        if msg in ('life'):
            return "My momma always said, “Life is like a box of chocolates, you never know what you’re gonna get."

        if msg in ('motivation', 'sad'):
            return "Don’t ever let somebody tell you you can’t do something, not even me. Alright? You dream, you gotta protect it. People can’t do something themselves, they wanna tell you you can’t do it. If you want something, go get it. Period."

        if msg in ('trust'):
            return "Someone in this camp ain't what he appears to be."

        if msg in ('funny'):
            return "It's just a flesh wound."
        
        if msg in ('bot'):
            return "I am t-800 cyberdyne systems model 101."
        
        if msg in ('serious'):
            return "I am serious. And don't call me Shirley."
        
        if user_message in ('fuck you', 'screw you', 'bad bot', 'f u'):
            return "I'm about to do to you what Limp Bizkit did to music in the late '90s."
        
        if msg in ('evil'):
            return "We get the warhead and we hold the world ransom for…. One million dollars."
        
        if msg in ('old'):
            return "It's not the years, honey. It's the mileage."
        
        if msg in ('question', 'asking'):
            return "You talkin to me?"
        
        if msg in ('die'):
            return "Yippie-ki-yay, motherf—er."
        
        if msg in ('war'):
            return "I love the smell of napalm in the morning."

        if msg in ('time'):
            now = datetime.now()
            date_time = now.strftime("%d/%m/%y, %H:%M:%S")

            return str(date_time)

    return "What?"
