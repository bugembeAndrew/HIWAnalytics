from __future__ import absolute_import
from django.conf import settings 
import twilio
import twilio.rest
from .models import Art, ArtCall

def send_twilio_message(to_number, body):
    client = twilio.rest.TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    
    return client.messages.create(
        body = body,
        to = to_number,
        from_ = settings.TWILIO_PHONE_NUMBER

        )


def send_individual_message_to_patient_whose_spouses_not_tested(id):
    client = twilio.rest.TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    qs = Art.objects.filter(artcall__spouse_tested = 'No', artcall__art__isnull = False).get(id)
    return client.messages.create(
        body = body, 
        to = qs.telephone_number,
        from_ = settings.TWILIO_PHONE_NUMBER

        )





