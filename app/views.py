from flask import Flask, render_template, make_response, flash, redirect, session, url_for, request, g
from app import app
from emails import contact_email
from forms import ContactForm


@app.route("/")
@app.route('/index', methods = ['GET', 'POST'])
def index():
		print "on index"
		return render_template("index.html")

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
        form = ContactForm()
        if form.validate_on_submit():
                contact_email(form.email.data, form.name.data, form.text.data)
                flash("Thanks for your feedback!")
                return redirect(url_for('index'))
        return render_template('contact.html', form = form)