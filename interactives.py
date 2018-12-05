import json
import uuid
import base64


class ReplyKeyboard:
    def __init__(self, key_constructor):
        if isinstance(key_constructor, dict):
            self.key_constructor = key_constructor
        else:
            raise Exception('except Dict receives {}'.format(str(type(key_constructor))))
        self.keyboard = key_constructor

    @property
    def keyboard(self):
        return json.dumps(self._keyboard)

    @keyboard.setter
    def keyboard(self, key_constructor):
        self._keyboard = {'keyboard': key_constructor}

    def reply_keyboard(self):
        keyboard = {'keyboard': self.key_constructor}
        return json.dumps(keyboard)


class InlineKeyboardButton:
    def __init__(self, text=None, cb_data=None):
        self.button = dict(text=str(text), cb_data=str(cb_data))

    def get_keyboard_dict(self):
        return self.button

    def __repr__(self):
        return json.dumps(self.button)


class InlineUrlButton:
    def __init__(self, text=None, url=None):
        self.button = dict(text=str(text), url=str(url))

    def get_keyboard_dict(self):
        return self.button

    def __repr__(self):
        return json.dumps(self.button)


class InlineInAppPurchaseButton:
    def __init__(self, text=None, amount=None, currency=None, desc=None):
        if currency not in ['IRR', 'coin']:
            raise Exception('currency must be IRR or coin')
        self.random_id = bytes(uuid.uuid4().hex, 'ascii')
        self.button = dict(text=str(text),
                           amount=int(amount),
                           currency=str(currency),
                           ref_id=base64.b64encode(self.random_id).decode('utf-8'),
                           desc=str(desc))

    def get_keyboard_dict(self):
        return self.button

    def __repr__(self):
        return json.dumps(self.button)
