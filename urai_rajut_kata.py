def urai(kalimatinput):
    hasil = ""
    # for ini untuk berapa kali penguraian akan dilakukan, dan penguraian akan dilakukan sebanyak length dari kalimat
    for i in range(0,len(kalimatinput)): 
        # for ini untuk menentukkan berapa huruf yang akan dicetak dalam seriap penguraian
        # yang akan dihasilkan pada looping 1 adalah : indeks 0 pada kalimat input
        # looping 2 adalah : indeks 0 sampai indeks i+1 pada kalimat input, dst untuk looping berikutnya
        for j in range(0,i+1): 
            hasil += f"{kalimatinput[j]}"
    return hasil

# untuk yang rajut jika dilihat dari indeks huruf yang akan diprint adalah indeks 0 2 5 9 14 20 dst
# jika dilihat setiap indeks yang akan di print 0 0+2 2+3 5+4 9+5 dst
def rajut(kalimatinput):
    indekstemp = 0 # indeks temp ini utuk menentukkan indeks huruf yang akan ditambahkan kehasil
    penambahan = 2 # variable ini untuk penambahan pada indeks yang akan ditambahkan ke hasil
    hasil2 = "" 
    # looping 1 : i = 0, i = indekstemp = 0, indeks i pada kalimatinput akan ditambahkan ke hasil, indekstemp = 2 dan pnembahan menjadi 3
    # looping 2 : i = 1 , i != indekstemp, maka indeks i pada kalimat input tidak akan ditambahkan ke hasil
    # looping 2 : i = 2, i = indekstemp = 2, indeks i pada kalimatinput akan ditambahkan ke hasil, indekstemp = 2 + 3 = 5 dan pnembahan menjadi 3 + 1 = 4
    # dst..     
    for i in range(0,len(kalimatinput)):
        if i == indekstemp:
            hasil2 += f"{kalimatinput[i]}"
            indekstemp += penambahan
            penambahan += 1
    return hasil2


print(urai("Code"))
print(urai("Python"))
print(urai("Purwadhika"))
print("")
print(rajut("CCoCodCode"))
print(rajut("PPyPytPythPythoPython"))
print(rajut("PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika"))