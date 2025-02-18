def bmsearch(text, pattern):

    last = buildLast(pattern) 
    n = len(text) # panjang text
    m = len(pattern) # panjang pattern
    i = m-1

    if (i > n-1):
        return -1 # kasus ketika panjang pattern > panjang text
    
    j = m-1
    while True:
        if (pattern[j].casefold() == text[i].casefold()):
            if (j == 0):
                return i
            else: # teknik looking glass
                i -= 1
                j -= 1
        else: # teknik character jump
            lastocc = last[ord(text[i])]
            i = i + m - min(j, 1+lastocc) # i baru
            j = m - 1 # j baru selalu dari karakter akhir pattern
        if (i > n-1 ):
            break
    return -1 # jika tidak ada yang pas

def buildLast(pattern):
    last = [-1] * 128 # inisialisasi array

    for i in range(len(pattern)):
        last[ord(pattern[i].casefold())] = i
    
    return last