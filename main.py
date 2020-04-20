from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        keyword = request.form.get("keyword")
        algo = request.form.get("algorithm")
        print(keyword)
        print(algo) 
    return render_template("mainpage.html")

@app.route("/about")
def about():
    return render_template("aboutpage.html")

if __name__ == "__main__":
    app.run(debug=True)