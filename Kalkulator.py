print ("===Kalkulator Sederhana")
number1 = int(input("Masukkan angka1: "))
number2 = int(input ("Masukkan Angka2: "))
#Pilih operasi yang diinginkan
print ("Pilih operasi")
print ("1. Operasi (+)")
print ("2. Operasi (-)")
print ("3. Operasi (*)")
print ("4. Operasi (/)")
#Pilihan operasi
pilihan = input ("Masukkan (1/2/3/4): ")
#percabangan. Pilih operasi yang diinginkan
if pilihan == "1":
    result = number1 + number2
    print(f"{number1} + {number2}= {result}")
elif pilihan == "2":
    result = number1 - number2
    print(f"{number1} - {number2}= {result}")
elif pilihan == "3":
    result = number1 * number2
    print(f"{number1} * {number2}= {result}")
elif pilihan =="4":
    #pembagian dengan 0 tidak diperbolehkan
    if number2 == 0:
        print("hasil tidak bisa ditentukan karena 0 tidak bisa berada di penyebut")
    else:
        result = number1 / number2
        print(f"{number1} / {number2}:{result}")
else:
    print("Pilihan tidak Valid")
    