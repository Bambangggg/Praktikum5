harga = 0
while True:
    umur_str = input("masukkan umur : ")
    if not umur_str :
        break
    umur = int(umur_str)
    #diubah ke int agar bisa lanjut ke kondisi if elif
    if umur <= 2 :
        print ("Gratis")
        print(f"Running Total : ${harga}")
    elif umur >= 3 and umur <= 12 :
        print ("Harga $14.00")
        harga += 14.00
        print(f"Running Total : ${harga}")
    elif umur >= 65:
        print("Harga $18.00")
        harga += 18.00
        print(f"Running Total : ${harga}")
    else :
        print("Harga $23.00")
        harga += 23.00
        print(f"Running Total : ${harga}")

uang = float(input("masukkan jumlah uang :"))
kembalian = uang - harga
print(f"Kembaliannya : ${kembalian}")
            
