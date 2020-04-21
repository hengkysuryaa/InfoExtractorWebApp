from flask import Flask, render_template, request, redirect
from nltk.tokenize import sent_tokenize
import kmp
import bm
import nearestUtil
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
                tanggal_artikel = regexmatch.searchtanggalartikel(sentences)
                for kal in sentences: # iterasi setiap kalimat pada text
                    if (algo == "kmp"):
                        pos = kmp.kmpsearch(kal, keyword)
                        if (pos != -1):
                            listangka = regexmatch.searchangka(kal) # search angka
                            posKeyword = kal.find(keyword)
                            angka = nearestUtil.nearestNum(listangka,posKeyword,kal) # angka terdekat
                            listtanggal = regexmatch.searchtanggal(kal) # search tanggal
                            if (len(listtanggal) == 0): # tidak ada tanggal di kalimat
                                tanggal = tanggal_artikel
                            else:
                                tanggal = regexmatch.firstTanggal(listtanggal)
                            kalimat = kal + ' (' + berkas.filename + ')'
                            item = {
                                    "Jumlah":angka,
                                    "Waktu":tanggal,
                                    "Kalimat":kalimat
                                    }
                            list.append(item)
                    if (algo == "bm"):
                        pos = bm.bmsearch(kal, keyword)
                        if (pos != -1):
                            listangka = regexmatch.searchangka(kal) # search angka
                            posKeyword = kal.find(keyword)
                            angka = nearestUtil.nearestNum(listangka,posKeyword,kal) # angka terdekat
                            listtanggal = regexmatch.searchtanggal(kal) # search tanggal
                            if (len(listtanggal) == 0): # tidak ada tanggal di kalimat
                                tanggal = tanggal_artikel
                            else:
                                tanggal = regexmatch.firstTanggal(listtanggal)
                            kalimat = kal + ' (' + berkas.filename + ')'
                            item = {
                                    "Jumlah":angka,
                                    "Waktu":tanggal,
                                    "Kalimat":kalimat
                                    }
                            list.append(item)
                    if (algo == "regex"):
                        pos = regexmatch.regexsearch(kal, keyword)
                        if (pos != -1):
                            listangka = regexmatch.searchangka(kal) # search angka
                            posKeyword = kal.find(keyword)
                            angka = nearestUtil.nearestNum(listangka,posKeyword,kal) # angka terdekat
                            listtanggal = regexmatch.searchtanggal(kal) # search tanggal
                            if (len(listtanggal) == 0): # tidak ada tanggal di kalimat
                                tanggal = tanggal_artikel
                            else:
                                tanggal = regexmatch.firstTanggal(listtanggal)
                            kalimat = kal + ' (' + berkas.filename + ')'
                            item = {
                                    "Jumlah":angka,
                                    "Waktu":tanggal,
                                    "Kalimat":kalimat
                                    }
                            list.append(item)
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename)) #hapus file yang diupload
        return render_template("mainpage.html",list = list)

@app.route("/about")
def about():
    return render_template("aboutpage.html")

if __name__ == "__main__":
    app.run(debug=True)