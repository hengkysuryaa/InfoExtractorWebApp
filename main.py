from flask import Flask, render_template, request
from nltk.tokenize import sent_tokenize
import kmp
import bm
import os

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        uploaded_files = request.form.getlist("file[]")
        for berkas in uploaded_files:
            with open('test/'+berkas, 'r') as file:
                text = file.read().replace('\n', ' ')
                sentences = sent_tokenize(text)
            keyword = request.form.get("keyword")
            algo = request.form.get("algorithm")
            for kal in sentences:
                if (algo == "kmp"):
                    pos = kmp.kmpsearch(kal, keyword)
                    if (pos != -1):
                        print(kal, end='')
                        print('(' + berkas + ')')
                if (algo == "bm"):
                    pos = bm.bmsearch(kal, keyword)
                    if (pos != -1):
                        print(kal, end='')
                        print('(' + berkas + ')')
                if (algo == "regex"):
                    print("regex")
    return render_template("mainpage.html")

@app.route("/about")
def about():
    return render_template("aboutpage.html")

if __name__ == "__main__":
    app.run(debug=True)