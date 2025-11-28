def hasil(p1, p2):
    if p1 == p2:
        return "Seri"
    elif (p1 == "Gunting" and p2 == "Kertas") or \
         (p1 == "Batu" and p2 == "Gunting") or \
         (p1 == "Kertas" and p2 == "Batu"):
        return "Pemain 1 Menang"
    else:
        return "Pemain 2 Menang"


while True:
    print("Pemain 1: Silahkan anda pilih : Gunting, Batu, Kertas -> ", end="")
    p1 = input().title()

    print("Pemain 2: Silahkan anda pilih : Gunting, Batu, Kertas -> ", end="")
    p2 = input().title()

    print(hasil(p1, p2))

    ulang = input("Apakah Anda Ingin memulai Permainan Awal lagi [Ya/y] atau [Tidak/t] -> ")
    if ulang.lower() not in ["ya", "y"]:
        break
