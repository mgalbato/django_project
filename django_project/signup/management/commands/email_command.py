from django.core.management.base import BaseCommand
from django.core import mail
from signup.models import City, Subscriber

# import sys
# sys.path.insert(1,'../../related')
from signup.related.weather import *

GOOD_SUBJECT = "It's nice out! Enjoy a discount on us."
BAD_SUBJECT = "Not so nice out? That's okay, enjoy a discount on us."
NEUTRAL_SUBJECT = "Enjoy a discount on us."

DESC_TXT = {
'Clear': 'clear skies',
'Thunderstorm': 'thunderstorms',
'Drizzle': 'some drizzling',
'Rain': 'rainy weather',
'Snow': 'snow',
'Clouds': 'clouds',
}

DESC_IMG = {
'Clear': 'https://gfycat.com/ifr/InconsequentialGrandioseConch',
'Thunderstorm': 'https://media.giphy.com/media/WoWpouO164dBS/giphy.gif',
'Drizzle': 'https://media.giphy.com/media/26uf5HjasTtxtNCqQ/giphy.gif',
'Rain': 'https://media.giphy.com/media/26uf5HjasTtxtNCqQ/giphy.gif',
'Snow': 'https://cdn.dribbble.com/users/2120934/screenshots/6193458/13_snow.gif',
'Clouds': 'https://media.giphy.com/media/4N1FZFE5AGO3qrUGkw/giphy.gif',
}

def gen_body(desc, high):
    if desc in DESC_TXT.keys():
        text = "Expect %s and a high of %s degrees" % (DESC_TXT[desc], high)
    else:
        text = "Today's High: %s degrees" % (high)
    if desc in DESC_IMG.keys():
        link = DESC_IMG[desc]
    else:
        link = ""
    body = """\
    <html>
      <head>
        <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,600" rel="stylesheet">
      </head>
      <body style="background-color: #EFEFEF">
        <h2 style="font-family: 'Open Sans', sans-serif;">%s</h2>
        <img style="width: 300px; height: 300px;" src="%s">
      </body>
    </html> """ % (text, link)
    return body

class Command(BaseCommand):
    help = 'Sends custom emails to all subscribers'

    def handle(self, *args, **kwargs):
        connection = mail.get_connection()
        connection.open()

        emails = []
        for sub in Subscriber.objects.all():
            weather = get_weather(sub.location.zip)
            enum = assign_enum(weather)
            if enum is Weather.GOOD:
                subject = GOOD_SUBJECT
            elif enum is Weather.BAD:
                subject = BAD_SUBJECT
            else:
                subject = NEUTRAL_SUBJECT
            body = gen_body(weather['today_desc'], weather['today_high'])

            email = mail.EmailMessage(subject, body, to=[sub.email])
            email.content_subtype = "html"
            emails.append(email)

        connection.send_messages(emails)
        connection.close()

        #try except for possible errors with sending emails?
        self.stdout.write(self.style.SUCCESS('Successfully sent custom emails to subscribers'))
        #count the number of invalid emails
