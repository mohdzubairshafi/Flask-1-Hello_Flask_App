# Step -1  To import Flask
from flask import Flask, request, render_template

# Step -2 Create Flask object with parameter __name__
app = Flask(__name__)

# Step -3  Create an End Points using routes and bind them with functionality


@app.route("/")
def index():
    username = request.args.get("username")
    if username:
        return render_template("UserDashboard.html", name=username.upper())
    return render_template("home.html")


# Step -4  run the app of name == main
if __name__ == "__main__":
    app.run(debug=True)
