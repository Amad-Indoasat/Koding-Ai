tanggal = int(input("Masukkan tanggal lahir: "))
bulan = int(input("Masukkan bulan lahir (1-12): "))

if bulan == 3 and tanggal >= 21 or bulan == 4 and tanggal <= 19:
    print("Aries")
elif bulan == 4 and tanggal >= 20 or bulan == 5 and tanggal <= 20:
    print("Taurus")
# Saya malas memasukkan zodiak lainnya
else:
    print("Zodiak tidak dikenali")