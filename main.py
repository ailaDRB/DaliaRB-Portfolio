from flask import Flask, request, render_template
import smtplib
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        comment = request.form["text"]
        try:
            send_email(name, email, comment)
            return "Email sent!"
        except Exception as e:
            return "Failed to send email: " + str(e)
        
    return """
        <form method="post">
            <input name="name" type="text" class="feedback-input" placeholder="Name" />   
            <input name="email" type="text" class="feedback-input" placeholder="Email" />
            <textarea name="text" class="feedback-input" placeholder="Comment"></textarea>
            <input type="submit" value="SUBMIT"/>
        </form>
    """

def send_email(name, email, comment):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(os.environ["GMAIL_USERNAME"], os.environ["GMAIL_PASSWORD"])
    message = "Name: {0}\nEmail: {1}\nComment: {2}".format(name, email, comment)
    server.sendmail(os.environ["GMAIL_USERNAME"], os.environ["GMAIL_USERNAME"], message)
    server.quit()

if __name__ == "__main__":
    app.run(debug=True)
     