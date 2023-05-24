from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "user page: " + name + " - " + str(id)


images = ["images/image1.jpg", "images/image2.jpg", "images/image3.jpg", "images/image4.jpg", "images/image5.jpg", "images/image6.jpg", "images/image7.jpg", "images/image8.jpg", "images/image9.jpg"]


@app.route("/galeria")
def galeria():
    return render_template("galeria.html", images=images)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        nick = request.form.get("nick")
        email = request.form.get("email")
        message = request.form.get("message")

        return render_template("contact.html", success=True)
    return render_template("contact.html", success=False)


if __name__ == "__main__":
    app.run(debug=True)