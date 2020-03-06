from django.core.mail import EmailMultiAlternatives
from django.template.loader import  render_to_string

def send_welcome_email(name,receiver):
    # creating message subject and sender
    subject = 'Welcome to the KUramzan business'
    sender = 'mwaigalo5@gmail.com'

    # passing in the context variable
    text_content = render_to_string('email/newsemail.txt', {"name: name"})
    html_content =  render_to_string('email/newsemail.html',{"name : name"})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()