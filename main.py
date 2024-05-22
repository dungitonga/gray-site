from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from os import environ


SENDER = "ianjecinta@gmail.com"
PASSWORD = environ.get("PASSWORD")
SUBJECT = "Readers Message"
RECIPIENT = "dungitonga.can@gmail.com"

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        sender = request.form['email']
        message = request.form['message']
        message_block = f"Readers name: {name}, email: {sender}, message: {message}"
        send_email(SUBJECT,message_block,SENDER,RECIPIENT,PASSWORD)
        return redirect("/")
    return render_template("index.html")

def send_email(subject,body,sender,recipient,password):

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = RECIPIENT
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipient, msg.as_string())

if __name__ == "__main__":
    app.run()
