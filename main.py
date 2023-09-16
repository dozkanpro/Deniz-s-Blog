from flask import Flask, render_template, request
import requests
import smtplib

my_email = 'denizkozkan@gmail.com'
posts = requests.get("https://api.npoint.io/6bbc25718782fbf15188", verify=False).json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request == "POST":
        data = request.form
        username = data.get("username")
        email = data.get("email")
        phone = data.get("phone")
        message = data.get("message")
        smtp_obj = smtplib.SMTP('localhost')
        smtp_obj.sendmail(email, my_email, message)
        return render_template("index.html")
    return render_template("contact.html")


@app.route("/articles")
def articles():
    return render_template("articles.html")


@app.route("/form-entry", methods=['GET', 'POST'])
def receive_data():
    data = request.form
    print(data["username"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
    return "<h1>Successfully sent your message</h1>"


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
