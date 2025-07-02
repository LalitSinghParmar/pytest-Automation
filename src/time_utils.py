from datetime import datetime

def get_greeting():
    now = datetime.now()
    if now.hour < 12:
        return "Good morning"
    elif now.hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"
