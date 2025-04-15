import sqlite3
import random

con=sqlite3.connect("database.db")
cursor=con.cursor()

def tablo_olustur():
    cursor.execute("DROP TABLE IF EXISTS Tablo")
    cursor.execute("CREATE TABLE IF NOT EXISTS Tablo (id integer primary key autoincrement ,x1 int ,y1 int,x2 int,y2 int)")
    con.commit()
def veri_ekle():
    adet = 0
    while adet < 100:
        x2 = random.randint(2, 1000)
        x1 = random.randint(1, x2 - 1)
        y2 = random.randint(2, 1000)
        y1 = random.randint(1, y2 - 1)

        if (x2 - x1) <= 100 and (y2 - y1) <= 100:
            cursor.execute("INSERT INTO Tablo (x1, y1, x2, y2) VALUES (?, ?, ?, ?)", (x1, y1, x2, y2))
            adet += 1

        con.commit()

def veri_al():
    cursor.execute("select *from tablo")
    liste = cursor.fetchall()
    # print("Dikdörtgen Koordinatları:")
    # for i in liste:
    #     print(i)

    return liste

def kesiyor_mu(d1,d2):
    if d1[3]<d2[1] or  d1[1]>d2[3] or  d1[4]<d2[2] or  d1[2]>d2[4]:
        return None
    else:
        return f"{d1[0]} id'li ({d1[1]},{d1[3]})-({d1[2]},{d1[4]}) dikdörtgeni ile {d2[0]} id'li ({d2[1]},{d2[3]})-({d2[2]},{d2[4]}) dikdörtgeni kesişmektedir "


def kapsiyor_mu(d1,d2):
    if d1[1]>=d2[1] and d1[2]>=d2[2] and  d1[3]<=d2[3] and d1[4]<=d2[4]:
        return f"{d1[0]} id'li ({d1[1]},{d1[3]})-({d1[2]},{d1[4]}) dikdörtgeni, {d2[0]} id'li ({d2[1]},{d2[3]})-({d2[2]},{d2[4]}) dikdörtgeni tarafından kapsanmaktadır "


def veri_kontrol(liste):
    temas_olan=[]
    for i in range(100):
        for j in range(i+1,100):
            sonuc1=kesiyor_mu(liste[i],liste[j])
            if sonuc1:
                # print(sonuc1)
                temas_olan.append(liste[i][0])
                temas_olan.append(liste[j][0])

            sonuc2=kapsiyor_mu(liste[i], liste[j])
            if sonuc2:
                print(sonuc2)
                temas_olan.append(liste[i][0])
                temas_olan.append(liste[j][0])

    for d in liste:
        if d[0] not in temas_olan:
            # print(f"{d[0]} id’li dikdörtgen hiçbir dikdörtgen ile temas etmemektedir.")
            pass

# tablo_olustur()
# veri_ekle()

# for row in cursor.execute("SELECT * FROM Tablo"):
#     print(row)

liste=veri_al()
veri_kontrol(liste)
















con.close()