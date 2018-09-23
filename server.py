from flask import *

app = Flask(__name__)
users = []


@app.route("/")
def index():
    return render_template("index.html", users_to_render=users)


@app.route("/add-user", methods=["POST"])
def add_user():
    username = request.form["username"]
    password = request.form["password"]
    users.append({"username":username, "password":password})
    return "successfull registration"

if __name__ == "__main__":
    app.run(debug=True)