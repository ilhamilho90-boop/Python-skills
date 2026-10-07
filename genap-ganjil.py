#Deteksi angka Ganjil dan Genap)
angka = int(input("Masukkan Angka : "))
if angka == 0 :
    print ("Bukan Angka Ganjil dan Genap")
elif angka % 2 == 0 :
    print("genap")
else :
    print ("ganjil")

