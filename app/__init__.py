from flask import Flask, render_template, make_response, flash, redirect, session, url_for, request, g

app = Flask(__name__)

@app.route("/")
def hello():
        user = g.user
        return render_template("index.html",
                title = maintitle)

if __name__ == "__main__":
    app.run()
