from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "chave_secreta_super_segura"

usuario = {
    "email": "marcos@gmail.com",
    "senha": generate_password_hash("205010")
}

MAX_TENTATIVAS = 3


@app.route("/", methods=["GET", "POST"])
def login():
    if "tentativas" not in session:
        session["tentativas"] = 0

    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        if session["tentativas"] >= MAX_TENTATIVAS:
            flash("Conta bloqueada por muitas tentativas!")
            return render_template("login.html")

        if email == usuario["email"] and check_password_hash(usuario["senha"], senha):
            session["usuario"] = email
            session["tentativas"] = 0
            return redirect(url_for("dashboard"))
        else:
            session["tentativas"] += 1
            flash(f"Email ou senha incorretos! Tentativas: {session['tentativas']}")

    return render_template("login.html")


@app.route("/dashboard.html")
def dashboard():
    if "usuario" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html", email=session["usuario"])


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True, port=5001)