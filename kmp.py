from nltk.tokenize import sent_tokenize

with open('text.txt', 'r') as file:
    text = file.read().replace('\n', ' ')

def kmp(text, pattern):
    n = len(text) # panjang text
    m = len(pattern) # panjang pattern

    list = fail(pattern) # tabel border function

    i = 0
    j = 0

    while (i < n):
        if (pattern[j].casefold() == text[i].casefold()):
            if (j == m-1):
                return i - m + 1 # cocok
            i += 1 # penggeseran karakter teks
            j += 1 # penggeseran karakter pattern
        elif (j>0):
            j = list[j-1] # penggeseran karakter pengecekan pada pattern sesuai nilai border function
        else:
            i += 1 # penggeseran karakter pengecekan pada teks
    
    return -1 # tidak cocok

def fail(pattern):

    list = [0] * (len(pattern)-1) # inisialisasi tabel

    m = len(pattern)
    j = 0
    i = 1

    while (i < m):
        if (pattern[j].casefold() == pattern[i].casefold()): # pemeriksaan pada karakter teks dan karakter pattern selanjutnya
            list[i] = j + 1
            i += 1
            j += 1
        elif (j>0): # pemeriksaan dimulai dari indeks ke-j dan i tidak berubah
            j = list[j-1]
        else: # pemeriksaan pada karakter teks selanjutnya, j = 0
            i += 1

    return list

def main(text, pattern):
    sentences = sent_tokenize(text)
    for kal in sentences:
        pos = kmp(kal, pattern)
        if (pos != -1):
            print(kal)
    
main(text, "Terkonfirmasi Positif")
