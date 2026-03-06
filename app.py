from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    comment = ""

    if request.method == "POST":
        comment = request.form.get("comment")

    return render_template("index.html", comment=comment)

if __name__ == "__main__":
    app.run(debug=True)