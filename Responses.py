from datetime import datetime

def responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup", "wassup", "what's up", "hello there!", "hello there"):
        return "General Kenobi!"

    if user_message in ("who are you", "who are you?"):
        return "I'm just a happy camper! Rockin' rollin'!"

    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "What?"
