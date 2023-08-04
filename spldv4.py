print("penyelesaian pada SPLDV")
print("ikuti langkah langkah di bawah ini dengan baik")
print("dan baca perintah di bawah ini ya")
print("jika error maka anda salah memasukan soal anda\n")
print("selamat mengerjakan!!\n")


#ini adalah data input atau bisa di bilanng soal
x = input("masukan nilai x pada baris pertama? ")
kal = input("apakah nilai y + (positif) atau - (negatif)? ")
y = input("masukan nilai y pada baris pertama? ")
jadi = input("masukan nilai = pada baris pertama? ")
print("========baris ke dua=======")

x2 = input("masukan nilai x pada kedua? ")
kal2 = input("apakah niali y + (positif) atau - (negatif)? ")
y2 = input("masukan nilai y pada baris kedua? ")
jadi2 = input("masukan nilai = pada baris kedua? \n")

#ini adalah hasil dari innput lalu di proses untuk menyelesaikan SPLDV


if kal == ("-"):
    if kal2 ==("-"):

        a = (int(x) * int(y2)) + (int(x2) * int(y))
        b = (int(y) * int(y2))  - (int(y2) * int(y))
        c = (int(jadi) * int(y2)) + (int(jadi2) * int(y))


if kal == ("+"):
    if kal2 ==("+"):

        a = (int(x) * int(y2)) - (int(x2) * int(y))
        b = (int(y) * int(y2))  - (int(y2) * int(y))
        c = (int(jadi) * int(y2)) - (int(jadi2) * int(y))

if kal == ("+"):
    if kal2 == ("-"):
        a = (int(x) * int(y2)) + (int(x2) * int(y))
        b = (int(y) * int(y2)) - (int(y2) * int(y))
        c = (int(jadi) * int(y2)) + (int(jadi2) * int(y))

if kal == ("-"):
    if kal2 == ("+"):
        a = (int(x) * int(y2)) + (int(x2) * int(y))
        b = (int(y) * int(y2)) - (int(y2) * int(y))
        c = (int(jadi) * int(y2)) + (int(jadi2) * int(y))


print("\n")
print("\n")

#ini untuk mencari nilai x

print(f"maka {x}x {kal} {y}y = {jadi}")
print(f"     {x2}x {kal2} {y2}y = {jadi2}\n")
lalu = int(c) / int(a)
print(f"jadi nilai x = {lalu}")

#ini untuk mencari nilai y

d = int(x) * int(lalu)
e = int(jadi) - int(d)
f = int(e) / int(y)
print (f"nilai y = {f}\n")

#ini adalah cara menghitungnya

print(f"untuk mencari x maka masing masing di kalikan dengan {y} dan {y2}")
print(F"lalu kita eliminasi y\n")
print(f"{x}x x{y2} {kal} {y}y x{y2} = {jadi} x{y2}")
print(f"{x2}x x{y} {kal2} {y2}y x{y} y = {jadi2} x{y}")
print(f"________________________________________________")
print(f"{a}x {b}y = {c}\n")
print(f"setelah itu x kita bagi dengan {c}")
print(f"x = {c}/{a}\n")
print(f"maka hasil dari x ={lalu}\n")

print(f"untuk mencari y yaitu dengan\n")
print(f"{x}({lalu}) {y}y = {jadi}")
print(f"{d} {kal} {y}y = {jadi}")
print(f"{y}y = {jadi} - {d}")
print(f"y = {e}/{y}\n")
print(f"jadi y = {f}")

