n = 0
jumlah = 0

while True:
    nilai = input("Masukkan nilai : ")
    
    if not nilai:
        break
    elif nilai == "A":
        jumlah += 1
        n += 4.00
        print("Nilai = 4.00")
    elif nilai == "A-":
        jumlah += 1
        n += 3.75
        print("Nilai = 3.75")
    elif nilai == "B+":
        jumlah += 1
        n += 3.50
        print("Nilai = 3.50")
    elif nilai == "B":
        jumlah += 1
        n += 3.00
        print("Nilai = 3.00")
    elif nilai == "C+":
        jumlah += 1
        n += 2.50
        print("Nilai = 2.50")
    elif nilai == "C":
        jumlah += 1
        n += 2.00
        print("Nilai = 2.00")
    elif nilai == "C-":
        jumlah += 1
        n += 1.75
        print("Nilai = 1.75")
    elif nilai == "D":
        jumlah += 1
        n += 1.50
        print("Nilai = 1.50")
    elif nilai == "E":
        jumlah += 1
        n += 1.25
        print("Nilai = 1.25")
    else:
        print("Input salah")

if jumlah == 0:
    print("nilai kosong")
else:
    rata_rata = n / jumlah
    print(f"Rata-rata nilai adalah: {rata_rata}")
