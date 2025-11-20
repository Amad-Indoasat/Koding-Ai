tahun = int(input("Masukkan tahun: "))

if (tahun % 400 == 0):
    print("Tahun Kabisat")
elif (tahun % 100 == 0):
    print("Bukan Tahun Kabisat")
elif (tahun % 4 == 0):
    print("Tahun Kabisat")
else:
    print("Bukan Tahun Kabisat")
