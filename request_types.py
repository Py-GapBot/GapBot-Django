from enum import Enum


class RequestType(Enum):
    member_join = 'join'
    member_leave = 'leave'
    text_message = 'text'
    image_message = 'image'
    audio_message = 'audio'
    video_message = 'video'
    voice_message = 'voice'
    receive_file = 'file'
    contact_message = 'contact'
    location_message = 'location'
    form = 'submitForm'
    inline_button = 'triggerButton'
    payment_info = 'paycallback'
    bill_info = 'invoicecallback'
