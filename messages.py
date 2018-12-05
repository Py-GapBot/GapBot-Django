import json
import requests
from request_types import RequestType


class Messages:
    def __init__(self, token, chat_id, reply_keyboard=None, inline_keyboard=None, form=None,
                 text=None, file=None, file_data=None, contact=None, location=None):
        self.header = {'token': str(token)}
        self.urls = {'send_message': 'https://api.gap.im/sendMessage',
                     'action': 'https://api.gap.im/sendAction',
                     'file_upload': 'https://api.gap.im/upload',
                     'edit_message': 'https://api.gap.im/editMessage',
                     'delete_message': 'https://api.gap.im/deleteMessage',
                     'answer_callback': 'https://api.gap.im/answerCallback',
                     'send_invoice': 'https://api.gap.im/invoice',
                     'invoice_inquiry': 'https://api.gap.im/invoice/inquery',
                     'verify_payment': 'https://api.gap.im/payment/verify',
                     'payment_inquiry': 'https://api.gap.im/payment/inquery'}
        self.chat_id = chat_id
        self.reply_keyboard = reply_keyboard
        self.inline_keyboard = inline_keyboard
        self.form = form
        self.message_text = text
        self.file = file  # file name or address on disk
        self.file_data = file_data  # type of Gap upload return json
        self.contact = contact
        self.location = location

    def send_message_json_data_maker(self, message_type):
        if message_type == RequestType['text_message'].value:
            return self.message_text
        elif (message_type == RequestType['image_message'].value
              or message_type == RequestType['audio_message'].value
              or message_type == RequestType['video_message'].value
              or message_type == RequestType['receive_file'].value
              or message_type == RequestType['voice_message'].value):
            return self.file_data
        elif message_type == RequestType['contact_message'].value:
            return self.contact
        elif message_type == RequestType['location_message'].value:
            return self.location
        elif message_type == 'action':
            return None

    def send_message_json_maker(self, message_type):
        data_dict = {'chat_id': self.chat_id,
                     'type': message_type,
                     'data': self.send_message_json_data_maker(message_type),
                     'reply_keyboard': self.reply_keyboard,
                     'inline_keyboard': self.inline_keyboard,
                     'form': self.form}
        return data_dict

    def send_message(self, message_type):
        """this method can send these types of messages:
        - text message
        - image message
        - video message
        - audio message
        - voice message
        - file
        - contact
        - location"""
        r = requests.post(url=self.urls['send_message'],
                          data=self.send_message_json_maker(message_type),
                          headers=self.header)
        if r.status_code == 200:
            return r.json()
        else:
            r.raise_for_status()

    def upload_file(self, file_type):
        file = {str(file_type): open(self.file, 'rb')}
        r = requests.post(url=self.urls['file_upload'], file=file, headers=self.header)
        if r.status_code == 200:
            return r.json()
        else:
            r.raise_for_status()

    def send_action(self):
        r = requests.post(url=self.urls['action'],
                          data=self.send_message_json_maker('action'),
                          headers=self.header)
        if not r:
            r.raise_for_status()

    def answer_callback(self, callback_id, text, show_alert=False):
        send_dict = {'chat_id': self.chat_id,
                     'callback_id': callback_id,
                     'text': text,
                     'show_alert': show_alert}
        r = requests.post(url=self.urls['answer_callback'],
                          data=send_dict,
                          headers=self.header)
        if not r:
            r.raise_for_status()

    def send_invoice(self, amount, description):
        send_dict = {'chat_id': self.chat_id,
                     'amount': amount,
                     'description': description}
        r = requests.post(url=self.urls['send_invoice'],
                          data=send_dict,
                          headers=self.header)
        if r:
            return r.json()['id']
        else:
            r.raise_for_status()

    def invoice_inquiry(self, ref_id):
        send_dict = {'chat_id': self.chat_id,
                     'ref_id': ref_id}
        r = requests.post(url=self.urls['invoice_inquiry'],
                          data=send_dict,
                          headers=self.header)
        if r:
            if r.json()['status'] == 'error':
                return 'error'
            elif r.json()['status'] == 'verified':
                return r.json()
        else:
            r.raise_for_status()

    def payment_inquiry(self, ref_id):
        send_dict = {'chat_id': self.chat_id,
                     'ref_id': ref_id}
        r = requests.post(url=self.urls['payment_inquiry'],
                          data=send_dict,
                          headers=self.header)
        if r:
            if r.json()['status'] == 'error':
                return 'error'
            elif r.json()['status'] == 'verified':
                return r.json()
        else:
            r.raise_for_status()
