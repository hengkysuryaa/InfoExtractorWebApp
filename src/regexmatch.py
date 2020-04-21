import re
from nltk.tokenize import sent_tokenize

with open('text2.txt', 'r') as file:
    text = file.read().replace('\n', ' ')

def searchangka(text):
    angka = re.findall(r'\s\d+[\,\.\d]\d*\s|^\d+\s', text)
    #'\d+[\,\.\d]\d*\s|\d+\s'
    # ([^\d]|^)\d{1,}[,.]\d{1,}([^\d]|$) --
    # ((\d|^)\d{0,}([^\d]|$))
    # ((\d|^)\d{0,})
    # (\s(\d|^)\d{0,}\s) --
    # ^\d+

    return angka

def searchtanggal(text):
    tanggal = re.findall(r'Senin.+[\)B]|Selasa.+[\)B]|Rabu.+[\)B]|Kamis.+[\)B]|Jumat.+[\)B]|Sabtu.+[\)B]|Minggu.+[\)B]|\d{1,2}\s\w+\s\d+|\d{1,2}\sJan\w*|\d{1,2}\sFeb\w*|\d{1,2}\sMar\w*|\d{1,2}\sApr\w*|\d{1,2}\sMei|\d{1,2}\sJun\w*|\d{1,2}\sJul\w*|\d{1,2}\sAg\w*|\d{1,2}\sSep\w*|\d{1,2}\sOkt\w*|\d{1,2}\sNov\w*|\d{1,2}\sDes\w*|kemarin|hari ini|besok|lusa', text)
    return tanggal

def searchtanggalartikel():
    sentences = sent_tokenize(text)
    found = False
    for kal in sentences:
        if re.findall(r'Senin.+[\)B]|Selasa.+[\)B]|Rabu.+[\)B]|Kamis.+[\)B]|Jumat.+[\)B]|Sabtu.+[\)B]|Minggu.+[\)B]',kal) and not(found):
            tanggalartikel = kal
            found = True # mencari tanggal artikel (di awal teks)
    return tanggalartikel

def regexmatch(text,pattern):
    sentences = sent_tokenize(text) # parsing kalimat
    for kal in sentences:
        if re.search(pattern,kal, re.I):
            angka = searchangka(kal)
            tanggal = searchtanggal(kal)
            for ang in angka:
                print(ang)
            
            if (len(tanggal) == 0):
                print(searchtanggalartikel())
            else:
                for tang in tanggal:
                    print(tang)
            print(kal)

regexmatch(text,'terkonfirmasi')