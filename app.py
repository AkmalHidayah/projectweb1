from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Masukkan kode autentikasi Anda di sini
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Masukkan kode pendaftaran Anda di sini
        return redirect(url_for("login"))
    return render_template("register.html")
@app.route("/event")
def event():
    return render_template("event.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/news")
def news():
    return render_template("news.html")
@app.route("/news")
def anggota():
    return render_template("anggota.php")

if __name__ == "__main__":
    app.run('0.0.0.0',port=5000,debug=True)
