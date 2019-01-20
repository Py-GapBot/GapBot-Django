from messages import Messages
from interactives import *
from form import *


class Handler:
    def __init__(self, message_type, chat_id, message_data, token, update_body):
        self.message_type = message_type
        self.chat_id = chat_id
        self.message_data = message_data
        self.bot_token = token
        self.update = update_body

    def run(self):
        {'join': self.join_member_handler(),
         'leave': self.leave_member_handler(),
         'text': self.text_message_handler(),
         'contact': self.contact_message_handler(),
         'location': self.location_message_handler(),
         'submitForm': self.form_handler(),
         'triggerButton': self.button_handler(),
         'paycallback': self.payment_handler(),
         'invoicecallback': self.bill_handler()}.get(self.message_type)

    def join_member_handler(self):
        pass  # todo: save for analyze

    def leave_member_handler(self):
        pass  # todo: save for analyze

    def text_message_handler(self):
        pass

    def contact_message_handler(self):
        pass

    def location_message_handler(self):
        pass

    def form_handler(self):
        pass

    def button_handler(self):
        pass

    def payment_handler(self):
        pass

    def bill_handler(self):
        pass
