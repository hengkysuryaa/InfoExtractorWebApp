from flask import Flask, render_template, request, redirect
from nltk.tokenize import sent_tokenize
import kmp
import bm
import regexmatch
import os
from werkzeug.utils import secure_filename

UPLOADER = os.path.dirname(os.path.abspath(__file__)) + '/upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOADER
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024 # maksimum file 8 mb

@app.route("/")
def home():
    return render_template("mainpage.html")

@app.route("/", methods=["POST"])
def submit():
    if request.method == "POST":
        list = []
        uploaded_files = request.files.getlist("file[]") # mengambil file yang diupload
        for berkas in uploaded_files:
            if berkas:
                filename = secure_filename(berkas.filename)
                berkas.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) # menyimpan berkas upload ke /upload
                with open('upload/'+berkas.filename, 'r') as file: # membaca file
                    text = file.read().replace('\n', ' ')
                    sentences = sent_tokenize(text) # parsing text menjadi kalimat
                keyword = request.form.get("keyword") # mengambil keyword masukan
                algo = request.form.get("algorithm") # mengambil pilihan algoritma
                for kal in sentences: # iterasi setiap kalimat pada text
                    if (algo == "kmp"):
                        pos = kmp.kmpsearch(kal, keyword)
                        if (pos != -1):
                            angka = regexmatch.searchangka(kal)
                            posKeyword = kal.find(keyword)
                            print(regexmatch.nearestNum(angka,posKeyword,kal))
                            print(kal, end='')
                            print('(' + berkas.filename + ')')
                    if (algo == "bm"):
                        pos = bm.bmsearch(kal, keyword)
                        if (pos != -1):
                            print(kal, end='')
                            print('(' + berkas.filename + ')')
                    if (algo == "regex"):
                        regexmatch.regexsearch(kal, keyword, berkas.filename, sentences)
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename)) #hapus file yang diupload
        
        tes = {
            "Jumlah":"13",
            "Waktu":"52",
            "Kalimat":"haha"
        }
        list.append(tes)
        tes2 = {
            "Jumlah":"14",
            "Waktu":"53",
            "Kalimat" : "hehe"
        }
        list.append(tes2)
        return render_template("resultpage.html",list = list)

@app.route("/about")
def about():
    return render_template("aboutpage.html")

if __name__ == "__main__":
    app.run(debug=True)