from flask.ext.mail import Message
from app import app,mail
from config import ADMINS
from flask import render_template
from threading import Thread
from decorators import async

@async
def send_async_email(msg):
        with app.app_context():
                mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
        msg = Message(subject, sender = sender, recipients = recipients)
        msg.body = text_body
        msg.html = html_body
        send_async_email(msg)

def contact_email(email, name, txt):
        print "Contact Email Sent"
        send_email("KenjinWeb | Contact Form",
                ADMINS[0],
                ADMINS,
                render_template("contact_email.txt", email = email,
                                                        name = name,
                                                        txt = txt),
                render_template("contact_email.html", email = email,
                                                        name = name,
                                                        txt = txt))

