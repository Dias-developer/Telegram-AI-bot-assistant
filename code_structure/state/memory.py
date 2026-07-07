history = {}

def get_history(user_id):
    return history.get(user_id, [])

def add_user_message(user_id, text):
    if user_id not in history:
        history[user_id] = []

    history[user_id].append({
        "role": "user",
        "text": text
    })
    history[user_id] = history[user_id][-20:]

def add_ai_message(user_id, text):
    if user_id not in history:
        history[user_id] = []

    history[user_id].append({
        "role": "model",
        "text": text
    })
    history[user_id] = history[user_id][-20:]