import os,time
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

KEY = 'Código Send Grid'

def send_email(link_of_page,name_of_file):
    # using SendGrid's Python Library
    # https://github.com/sendgrid/sendgrid-python
    message = Mail(
        from_email='do email x do send grid',
        to_emails='para email y',
        subject='Nova alteração no site do '+name_of_file,
        html_content='Acesse: '+link_of_page)
    try:
        sg = SendGridAPIClient(KEY)
        response = sg.send(message)
        
    except Exception as e:
        print('Email não Enviado')