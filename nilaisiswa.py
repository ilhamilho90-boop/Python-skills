print("=== Menghitung Nilai Siswa ===")
#daftar nilai siswa
nilai_siswa = []
#Input Jumlah siswa
jumlah = int(input("Masukkan Jumlah Siswa: "))
#Perulangan for diulang sebanyak jumlah siswa
for i in range(jumlah):
    #perulangan while, meminta input nilai sampai memnuhi
    while True:
        nilai =int(input(f"Nilai siswa ke-{i + 1}: "))
        if nilai >= 0 and nilai <= 100:
            break #Nilai tidak valid
        print("Nilai harus antara 0 sampai 100, coba lagi")
        #append() menambah nilai ke akhir list
    nilai_siswa.append(nilai)
#hitung statistika menggunakan fungsi bawaan
total=sum(nilai_siswa)
rata_rata=total/len(nilai_siswa)
tertinggi=max(nilai_siswa)
terendah=min(nilai_siswa)
print("==Hasil==")
print("Daftar Nilai:",nilai_siswa)
print("Rata-rata:",rata_rata)
print("Tertinggi:",tertinggi)
print("terendah:",terendah)
#Hitung nilai siswa yang lulus dan tidak lulus
batas_lulus = 75
lulus = 0
for nilai in nilai_siswa:
    if nilai >= batas_lulus:
     lulus += 1
tidak_lulus = len(nilai_siswa) - lulus
print ("Jumlah lulus:", lulus)
print ("Tidak lulus:", tidak_lulus)
#tampilkan predikat setiap siswa
print ("==Predika==")
for i, nilai in enumerate (nilai_siswa):
    if nilai >=90 :
        predikat = "A"
    elif nilai >= 80:
        predikat = "B"
    elif nilai >= 75:
        predikat ="C"
    elif nilai < 75:
        predikat = "D"
    else :
        predikat = "E"
    print(f"siswa ke-{i + 1}:{nilai} {predikat} ")