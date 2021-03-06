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

#logging
if not app.debug:
        import logging
        from logging.handlers import RotatingFileHandler
        file_handler = RotatingFileHandler('tmp/kenjinweb.log', 'a', 1 * 1024 * 1024, 10)
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        app.logger.setLevel(logging.INFO)
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.info('kenjinweb startup')


from app import views