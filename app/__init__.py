from flask import Flask
from flask.ext.mail import Mail
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD

app = Flask(__name__)
app.config.from_object('config')
mail = Mail(app)

#error emails
if not app.debug:
        import logging
        from logging.handlers import SMTPHandler
        if MAIL_USERNAME or MAIL_PASSWORD:
                credentials = (MAIL_USERNAME, MAIL_PASSWORD)
        mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT),
                 'no-reply@' + MAIL_SERVER,
                 ADMINS,
                 'KenjinWebFailure',
                 credentials)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

from app import views