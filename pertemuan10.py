pilihan = int (input ("1 = menghitung luas persegi 2 = menghitung luas lingkaran 3 = menghitung luas segitiga 4 = menghitung luas layang layang 5 = menghitung luas jajar genjang "))
    
match pilihan :
        case 1 :
            print ("menghitung luas persegi")
            s = int (input("masukan sisi :"))
            LuasPersegi = s * s
            print (f"Luas persegi dengan sisi {s} adalah {LuasPersegi}")
        case 2 :
            print ("menghitung luas lingkaran")
            pi : 3.14
            r = int(input("masukan rusuk lingkaran"))
            LuasLingkaran = pi * r ** 2
            print (f"luas lingkaran dengan rusuk {r} adalah {LuasLingkaran}")
        case 3 :
            print ("menghitung luas segitiga")
            alas = int(input("masukan alas segitiga"))
            tinggi = int(input("masukan tinggi segitiga"))
            LuasSegitiga = 1/2 * alas * tinggi
            print (f"luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {LuasSegitiga}")
        case 4 :
            print ("menghitung luas Layang Layang")
            d1 = int(input("diagonal 1"))
            d2 = int(input("diagonal 2"))
            LuasLayangLayang = 1/2 * d1 * d2
            print (f"luas layang layang dengan diagonal 1 {d1} dan diagonal 2 {d2} adalah {LuasLayangLayang}")
        case 5 :
            print ("menghitung luas Jajar Genjang")
            alas = int(input("masukan alas Jajar genjang"))
            tinggi = int(input("masukan tinggi Jajar genjang"))
            LuasJajarGenjang = alas * tinggi
            print (f"luas Jajar genjang dengan alas {alas} dan tinggi {tinggi} adalah {LuasJajarGenjang}")
        case _:
            print ("input tidak valid")