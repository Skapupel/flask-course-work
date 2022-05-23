

class Message():
    json = None
    chat_id = None
    message_id = None
    username = None
    text = None
    photo = None
    document = None
    data = None

    def __init__(self, json):
        self.json = json

    @property
    def chat_id(self):
        try:
            if list(self.json.keys())[1] == 'message':
                return self.json['message']['chat']['id']
            else:
                return self.json['callback_query']['message']['chat']['id']
        except:
            return None

    @property
    def message_id(self):
        try:
            if list(self.json.keys())[1] == 'message':
                return self.json['message']['message_id']
            else:
                return self.json['callback_query']['message']['message_id']
        except:
            return None
    
    @property
    def username(self):
        try:
            if list(self.json.keys())[1] == 'message':
                return self.json['message']['chat']['username']
            else:
                return self.json['callback_query']['message']['chat']['username']
        except:
            return None

    @property
    def text(self):
        try:
            if list(self.json.keys())[1] == 'message':
                return self.json['message']['text']
            else:
                return self.json['callback_query']['message']['text']
        except:
            return None

    @property
    def photo(self):
        try:
            return self.json[list(self.json.keys())[1]]['photo']
        except:
            return None

    @property
    def document(self):
        try:
            return self.json[list(self.json.keys())[1]]['document']
        except:
            return None
    
    @property
    def data(self):
        try:
            if list(self.json.keys())[1] == 'callback_query':
                return self.json['callback_query']['data']
            else:
                return None
        except:
            return None


class CallbackQuery():
    json = None
    data = None



def createKeyboardButton(text, callback_data):
    return {
        "text": text,
        "callback_data": callback_data
    }


def createKeyboardMarkup(buttons):
    return {
        "inline_keyboard": [
            [button] for button in buttons
        ]
    }