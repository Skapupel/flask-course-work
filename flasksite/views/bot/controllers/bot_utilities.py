

class Message():
    json = None
    chat_id = None
    username = None
    text = None
    photo = None
    document = None

    def __init__(self, json):
        self.json = json

    @property
    def chat_id(self):
        try:
            return self.json['message']['chat']['id']
        except:
            return None
    
    @property
    def username(self):
        try:
            return self.json['message']['chat']['username']
        except:
            return None

    @property
    def text(self):
        try:
            return self.json['message']['text']
        except:
            return None

    @property
    def photo(self):
        try:
            return self.json['message']['photo']
        except:
            return None

    @property
    def document(self):
        try:
            return self.json['message']['document']
        except:
            return None