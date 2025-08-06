from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()  # Load environment variables from .env

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    receiver_email = request.form['email']
    user_message = request.form['message']

    sender_email = os.getenv("EMAIL")
    app_password = os.getenv("APP_PASSWORD")

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = f"Message from {name}"

    body = f"Name: {name}\n\nMessage:\n{user_message}"
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        result_message = "✅ Email sent successfully!"
        result_class = "success"
    except Exception as e:
        result_message = f"❌ Failed to send email. Error: {str(e)}"
        result_class = "danger"

    return render_template("form.html", result_message=result_message, result_class=result_class)


if __name__ == '__main__':
    app.run(debug=True)
