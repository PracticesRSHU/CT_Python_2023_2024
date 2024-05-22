import requests
from time import sleep

# url ="https://api.telegram.org/bot941716973:AAHLtCFRXUuBe8eKFkPAPlEDnRoGjokFO5M
# /" #token's bot, наприклад, 
url = "https://api.telegram.org/bot7068771712:AAFeQBh6MSQTLO5tBnbWk5Ny1CSadzIe2AY/"

def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response



def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
            send_mess(get_chat_id(last_update(get_updates_json(url))), last_update(get_updates_json(url))['message']['text'])
            update_id += 1
        sleep(5)
if __name__ == '__main__':
    main()
    # chat_id = get_chat_id(last_update(get_updates_json(url)))
    # send_mess(chat_id, 'Hello! How are you?')