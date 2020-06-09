from flask import Flask, request, redirect, url_for
from flask import render_template
import os
import sqlite3
import pandas as pd
import numpy as np
import os.path

app = Flask(__name__)

db_name='baza.db'
path='C:\\Users\\matij\\Documents\\STUDIA\\Semestr 4 (xml,Java+SQL)\\Aplikacje bazodanowe\\venv\\lab13_projekt2\\'
spr = os.path.isfile(path+db_name) 
if spr==True:
    con = sqlite3.connect(db_name)
    print("Połączono z bazą danych")
else:
    print("Brak połączenia z bazą danych")


cur = con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_names = cur.fetchall()

cur.execute("SELECT name FROM sqlite_master WHERE type='view';")
view_names = cur.fetchall()

con.row_factory = sqlite3.Row
cur = con.cursor()
 
## kod byłby o połowę krótszy gdyby sqlite pozwalał na podawanie nazwy kolumn i tabel jako parametru funkcji

'''
def crt_table(tablename):
    params = (tablename,)
    func = ("""
    SELECT * FROM @tablename
    """)

    cur.execute(func,params)
    row = cur.fetchone()
    names = row.keys()
    naglowek = []
    for row in names:
        naglowek.append(row)
    naglowek=tuple(i for i in naglowek)                               
    cur.execute(func,params)
    osoby = cur.fetchall()
    rekordy=[]
    rekordy.append(naglowek)    
    for row in osoby:
        rekordy.append(tuple(row))
    data_array=np.array(rekordy)

    return data_array
'''
#print(table_names[0][0])
#print(crt_table(table_names[0][0]))

#ADRES
def adres_show():
    cur.execute("""
        SELECT * FROM Adres
    """)
    row = cur.fetchone()
    names = row.keys()
    naglowek = []
    for row in names:
        naglowek.append(row)
    naglowek=tuple(i for i in naglowek)                               
    cur.execute("""
        SELECT * FROM Adres
    """)
    osoby = cur.fetchall()
    rekordy=[]
    rekordy.append(naglowek)    
    for row in osoby:
        rekordy.append(tuple(row))
    return np.array(rekordy)
def adres_insert(miejsc,ulica,nrD,nrM,kod):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    #print("Podane dane to: " + str(miejsc) + str(ulica) + str(nrD) + str(nrM) + str(kod))
    cur.execute('INSERT INTO Adres VALUES(NULL, ?, ?, ?, ?, ?)', (miejsc, ulica, nrD, nrM, kod))
    con.commit()
    return redirect(url_for("tabela_adres"))
def adres_del(id):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    cur.execute('DELETE FROM Adres WHERE idAdres= ? ',(id,))
    con.commit()
    return redirect(url_for("tabela_adres"))
def adres_alter(id,col,val):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    if col=='miejscowosc':
        cur.execute("UPDATE Adres SET miejscowosc = ? WHERE idAdres = ?",(val,id))
    if col=='ulica':
        cur.execute("UPDATE Adres SET ulica = ? WHERE idAdres = ?",(val,id))
    if col=='nr_domu':
        cur.execute("UPDATE Adres SET nr_domu = ? WHERE idAdres = ?",(val,id))
    if col=='nr_mieszkania':
        cur.execute("UPDATE Adres SET nr_mieszkania = ? WHERE idAdres = ?",(val,id))
    if col=='kod':
        cur.execute("UPDATE Adres SET kod = ? WHERE idAdres = ?",(val,id))    
    con.commit()
    return redirect(url_for("tabela_adres"))   
adres_array=adres_show()

#ZNIZKA
def znizka_show():
    cur.execute("""
        SELECT * FROM Znizka
    """)
    row = cur.fetchone()
    names = row.keys()
    naglowek = []
    for row in names:
        naglowek.append(row)
    naglowek=tuple(i for i in naglowek)                               
    cur.execute("""
        SELECT * FROM Znizka
    """)
    osoby = cur.fetchall()
    rekordy=[]
    rekordy.append(naglowek)    
    for row in osoby:
        rekordy.append(tuple(row))
    return np.array(rekordy)
def znizka_insert(nazwa,prR):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    cur.execute('INSERT INTO Znizka VALUES(NULL, ?, ?)', (nazwa, prR))
    con.commit()
    return redirect(url_for("tabela_znizka"))
def znizka_del(id):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    cur.execute('DELETE FROM Znizka WHERE idZnizka= ? ',(id,))
    con.commit()
    return redirect(url_for("tabela_znizka"))
def znizka_alter(id,col,val):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    if col=='nazwa':
        cur.execute("UPDATE Znizka SET nazwa = ? WHERE idZnizka = ?",(val,id))
    if col=='procentRabatu':
        cur.execute("UPDATE Znizka SET procentRabatu = ? WHERE idZnizka = ?",(val,id))
    con.commit()
    return redirect(url_for("tabela_znizka"))   
znizka_array=znizka_show()

#OCENA
def ocena_show():
    cur.execute("""
        SELECT * FROM Ocena
    """)
    row = cur.fetchone()
    names = row.keys()
    naglowek = []
    for row in names:
        naglowek.append(row)
    naglowek=tuple(i for i in naglowek)                               
    cur.execute("""
        SELECT * FROM Ocena
    """)
    osoby = cur.fetchall()
    rekordy=[]
    rekordy.append(naglowek)    
    for row in osoby:
        rekordy.append(tuple(row))
    return np.array(rekordy)
def ocena_insert(ocK,pP):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    cur.execute('INSERT INTO Ocena VALUES(NULL, ?, ?)', (ocK, pP))
    con.commit()
    return redirect(url_for("tabela_ocena"))
def ocena_del(id):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    cur.execute('DELETE FROM Ocena WHERE idOcena= ? ',(id,))
    con.commit()
    return redirect(url_for("tabela_ocena"))
def ocena_alter(id,col,val):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    if col=='ocenaKierowcy':
        cur.execute("UPDATE Ocena SET ocenaKierowcy = ? WHERE idOcena = ?",(val,id))
    if col=='podwyzkaProcent':
        cur.execute("UPDATE Ocena SET podwyzkaProcent = ? WHERE idOcena = ?",(val,id))
    con.commit()
    return redirect(url_for("tabela_ocena"))   
ocena_array = ocena_show()

#KLIENT
def klient_show():
    cur.execute("""
        SELECT * FROM Klient
    """)
    row = cur.fetchone()
    names = row.keys()
    naglowek = []
    for row in names:
        naglowek.append(row)
    naglowek=tuple(i for i in naglowek)                               
    cur.execute("""
        SELECT * FROM Klient
    """)
    osoby = cur.fetchall()
    rekordy=[]
    rekordy.append(naglowek)    
    for row in osoby:
        rekordy.append(tuple(row))
    return np.array(rekordy)
def klient_insert(a1,a2,a3,idZ,imie,nazwisko,dataUr):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    cur.execute('INSERT INTO Klient VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)', (a1,a2,a3,idZ,imie,nazwisko,dataUr))
    con.commit()
    return redirect(url_for("tabela_klient"))
def klient_del(id):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    cur.execute('DELETE FROM Klient WHERE idKlient= ? ',(id,))
    con.commit()
    return redirect(url_for("tabela_klient"))
def klient_alter(id,col,val):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    if col=='Adres3':
        cur.execute("UPDATE Klient SET Adres3 = ? WHERE idKlient = ?",(val,id))
    if col=='Adres2':
        cur.execute("UPDATE Klient SET Adres2 = ? WHERE idKlient = ?",(val,id))
    if col=='Adres1':
        cur.execute("UPDATE Klient SET Adres1 = ? WHERE idKlient = ?",(val,id))
    if col=='idZnizka':
        cur.execute("UPDATE Klient SET idZnizka = ? WHERE idKlient = ?",(val,id))
    if col=='imie':
        cur.execute("UPDATE Klient SET imie = ? WHERE idKlient = ?",(val,id))
    if col=='nazwisko':
        cur.execute("UPDATE Klient SET nazwisko = ? WHERE idKlient = ?",(val,id))
    if col=='dataUrodzenia':
        cur.execute("UPDATE Klient SET dataUrodzenia = ? WHERE idKlient = ?",(val,id))       
    con.commit()
    return redirect(url_for("tabela_klient"))   
klient_array = klient_show()

#KIEROWCA
def kierowca_show():
    cur.execute("""
        SELECT * FROM Kierowca
    """)
    row = cur.fetchone()
    names = row.keys()
    naglowek = []
    for row in names:
        naglowek.append(row)
    naglowek=tuple(i for i in naglowek)                               
    cur.execute("""
        SELECT * FROM Kierowca
    """)
    osoby = cur.fetchall()
    rekordy=[]
    rekordy.append(naglowek)    
    for row in osoby:
        rekordy.append(tuple(row))
    return np.array(rekordy)
def kierowca_insert(idO,aT,aS,aK,imie,nazwisko,dost):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    cur.execute('INSERT INTO Kierowca VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)', (idO,aT,aS,aK,imie,nazwisko,dost))
    con.commit()
    return redirect(url_for("tabela_kierowca"))
def kierowca_del(id):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    cur.execute('DELETE FROM Kierowca WHERE idKierowca= ? ',(id,))
    con.commit()
    return redirect(url_for("tabela_kierowca"))
def kierowca_alter(id,col,val):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    if col=='idOcena':
        cur.execute("UPDATE Kierowca SET idOcena = ? WHERE idKierowca = ?",(val,id))
    if col=='adresTymcz':
        cur.execute("UPDATE Kierowca SET adresTymcz = ? WHERE idKierowca = ?",(val,id))
    if col=='adresStaly':
        cur.execute("UPDATE Kierowca SET adresStaly = ? WHERE idKierowca = ?",(val,id))
    if col=='adresKorespondencji':
        cur.execute("UPDATE Kierowca SET adresKorespondencji = ? WHERE idKierowca = ?",(val,id))
    if col=='imie':
        cur.execute("UPDATE Kierowca SET imie = ? WHERE idKierowca = ?",(val,id))
    if col=='nazwisko':
        cur.execute("UPDATE Kierowca SET nazwisko = ? WHERE idKierowca = ?",(val,id))
    if col=='czyDostepny':
        cur.execute("UPDATE Kierowca SET czyDostepny = ? WHERE idKierowca = ?",(val,id))       
    con.commit()
    return redirect(url_for("tabela_kierowca"))   
kierowca_array = kierowca_show()

#RODZAJ SAMOCHODU
def rodzsam_show():
    cur.execute("""
        SELECT * FROM Rodzaj_samochodu
    """)
    row = cur.fetchone()
    names = row.keys()
    naglowek = []
    for row in names:
        naglowek.append(row)
    naglowek=tuple(i for i in naglowek)                               
    cur.execute("""
        SELECT * FROM Rodzaj_samochodu
    """)
    osoby = cur.fetchall()
    rekordy=[]
    rekordy.append(naglowek)    
    for row in osoby:
        rekordy.append(tuple(row))
    return np.array(rekordy)
def rodzsam_insert(marka,model,ilM,cZK):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    cur.execute('INSERT INTO Rodzaj_samochodu VALUES(NULL, ?, ?,?,?)', (marka,model,ilM,cZK))
    con.commit()
    return redirect(url_for("tabela_rodzsam"))
def rodzsam_del(id):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    cur.execute('DELETE FROM Rodzaj_samochodu WHERE idRodzaj_samochodu= ? ',(id,))
    con.commit()
    return redirect(url_for("tabela_rodzsam"))
def rodzsam_alter(id,col,val):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    if col=='marka':
        cur.execute("UPDATE Rodzaj_samochodu SET marka = ? WHERE idRodzaj_samochodu = ?",(val,id))
    if col=='model':
        cur.execute("UPDATE Rodzaj_samochodu SET model = ? WHERE idRodzaj_samochodu = ?",(val,id))
    if col=='iloscMiejsc':
        cur.execute("UPDATE Rodzaj_samochodu SET iloscMiejsc = ? WHERE idRodzaj_samochodu = ?",(val,id))
    if col=='cenaZaKm':
        cur.execute("UPDATE Rodzaj_samochodu SET cenaZaKm = ? WHERE idRodzaj_samochodu = ?",(val,id))
    con.commit()
    return redirect(url_for("tabela_rodzsam"))   
rodzsam_array = rodzsam_show()

#EGZEMPLARZ
def egzemplarz_show():
    cur.execute("""
        SELECT * FROM Egzemplarz
    """)
    row = cur.fetchone()
    names = row.keys()
    naglowek = []
    for row in names:
        naglowek.append(row)
    naglowek=tuple(i for i in naglowek)                               
    cur.execute("""
        SELECT * FROM Egzemplarz
    """)
    osoby = cur.fetchall()
    rekordy=[]
    rekordy.append(naglowek)    
    for row in osoby:
        rekordy.append(tuple(row))
    return np.array(rekordy)
def egzemplarz_insert(idK,idRs,unNr,kolor,ocS):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    cur.execute('INSERT INTO Egzemplarz VALUES(?,?,?,?,?)', (idK,idRs,unNr,kolor,ocS))
    con.commit()
    return redirect(url_for("tabela_egzemplarz"))
def egzemplarz_del(id):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    cur.execute('DELETE FROM Egzemplarz WHERE idEgzemplarz= ? ',(id,))
    con.commit()
    return redirect(url_for("tabela_egzemplarz"))
def egzemplarz_alter(id,col,val):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    if col=='idKierowca':
        cur.execute("UPDATE Egzemplarz SET idKierowca = ? WHERE idEgzemplarz = ?",(val,id))
    if col=='idRodzaj_samochodu':
        cur.execute("UPDATE Egzemplarz SET idRodzaj_samochodu = ? WHERE idEgzemplarz = ?",(val,id))
    if col=='unikalnyNr':
        cur.execute("UPDATE Egzemplarz SET unikalnyNr = ? WHERE idEgzemplarz = ?",(val,id))
    if col=='kolor':
        cur.execute("UPDATE Egzemplarz SET kolor = ? WHERE idEgzemplarz = ?",(val,id))
    if col=='ocenaSamoch':
        cur.execute("UPDATE Egzemplarz SET ocenaSamoch = ? WHERE idEgzemplarz = ?",(val,id))
    con.commit()
    return redirect(url_for("tabela_egzemplarz"))   
egzemplarz_array = egzemplarz_show()

#OPLATA
def oplata_show():
    cur.execute("""
        SELECT * FROM Oplata
    """)
    row = cur.fetchone()
    names = row.keys()
    naglowek = []
    for row in names:
        naglowek.append(row)
    naglowek=tuple(i for i in naglowek)                               
    cur.execute("""
        SELECT * FROM Oplata
    """)
    osoby = cur.fetchall()
    rekordy=[]
    rekordy.append(naglowek)    
    for row in osoby:
        rekordy.append(tuple(row))
    return np.array(rekordy)
def oplata_insert(formaP,opD):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    cur.execute('INSERT INTO Oplata VALUES(NULL, ?, ?)', (formaP,opD))
    con.commit()
    return redirect(url_for("tabela_oplata"))
def oplata_del(id):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    cur.execute('DELETE FROM Oplata WHERE idOplata= ? ',(id,))
    con.commit()
    return redirect(url_for("tabela_oplata"))
def oplata_alter(id,col,val):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    if col=='formaPlatnosci':
        cur.execute("UPDATE Oplata SET formaPlatnosci = ? WHERE idOplata = ?",(val,id))
    if col=='oplataDodatk':
        cur.execute("UPDATE Oplata SET oplataDodatk = ? WHERE idOplata = ?",(val,id))
    con.commit()
    return redirect(url_for("tabela_oplata"))   
oplata_array = oplata_show()

#TARYFA
def taryfa_show():
    cur.execute("""
        SELECT * FROM Taryfa
    """)
    row = cur.fetchone()
    names = row.keys()
    naglowek = []
    for row in names:
        naglowek.append(row)
    naglowek=tuple(i for i in naglowek)                               
    cur.execute("""
        SELECT * FROM Taryfa
    """)
    osoby = cur.fetchall()
    rekordy=[]
    rekordy.append(naglowek)    
    for row in osoby:
        rekordy.append(tuple(row))
    return np.array(rekordy)
def taryfa_insert(nazwa,wysT):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    cur.execute('INSERT INTO Taryfa VALUES(NULL, ?, ?)', (nazwa,wysT))
    con.commit()
    return redirect(url_for("tabela_taryfa"))
def taryfa_del(id):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    cur.execute('DELETE FROM Taryfa WHERE idTaryfa= ? ',(id,))
    con.commit()
    return redirect(url_for("tabela_taryfa"))
def taryfa_alter(id,col,val):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    if col=='nazwa':
        cur.execute("UPDATE Taryfa SET nazwa = ? WHERE idTaryfa = ?",(val,id))
    if col=='wysokoscTaryfy':
        cur.execute("UPDATE Taryfa SET wysokoscTaryfy = ? WHERE idTaryfa = ?",(val,id))
    con.commit()
    return redirect(url_for("tabela_taryfa"))   
taryfa_array = taryfa_show()

#KURS
def kurs_show():
    cur.execute("""
        SELECT * FROM Kurs
    """)
    row = cur.fetchone()
    names = row.keys()
    naglowek = []
    for row in names:
        naglowek.append(row)
    naglowek=tuple(i for i in naglowek)                               
    cur.execute("""
        SELECT * FROM Kurs
    """)
    osoby = cur.fetchall()
    rekordy=[]
    rekordy.append(naglowek)    
    for row in osoby:
        rekordy.append(tuple(row))
    return np.array(rekordy)
def kurs_insert(idO,idT,idKier,idKl,lokK,lokP,dataK,godzPocz,godzKonc,ocP,komP,laczna):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    cur.execute('INSERT INTO Kurs VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (idO,idT,idKier,idKl,lokK,lokP,dataK,godzPocz,godzKonc,ocP,komP,laczna))
    con.commit()
    return redirect(url_for("tabela_kurs"))
def kurs_del(id):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    cur.execute('DELETE FROM Kurs WHERE idKurs= ? ',(id,))
    con.commit()
    return redirect(url_for("tabela_kurs"))
def kurs_alter(id,col,val):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    if col=='idOplata':
        cur.execute("UPDATE Kurs SET idOplata = ? WHERE idKurs = ?",(val,id))
    if col=='idTaryfa':
        cur.execute("UPDATE Kurs SET idTaryfa = ? WHERE idKurs = ?",(val,id))
    if col=='idKierowca':
        cur.execute("UPDATE Kurs SET idKierowca = ? WHERE idKurs = ?",(val,id))
    if col=='idKlient':
        cur.execute("UPDATE Kurs SET idKlient = ? WHERE idKurs = ?",(val,id))
    if col=='lokalizacjaKonc':
        cur.execute("UPDATE Kurs SET lokalizacjaKonc = ? WHERE idKurs = ?",(val,id))
    if col=='lokalizacjaPocz':
        cur.execute("UPDATE Kurs SET lokalizacjaPocz = ? WHERE idKurs = ?",(val,id))
    if col=='dataKursu':
        cur.execute("UPDATE Kurs SET dataKursu = ? WHERE idKurs = ?",(val,id))
    if col=='godzinaPocz':
        cur.execute("UPDATE Kurs SET godzinaPocz = ? WHERE idKurs = ?",(val,id))
    if col=='godzinaKonc':
        cur.execute("UPDATE Kurs SET godzinaKonc = ? WHERE idKurs = ?",(val,id))
    if col=='ocenaPrzejazdu':
        cur.execute("UPDATE Kurs SET ocenaPrzejazdu = ? WHERE idKurs = ?",(val,id))
    if col=='komentarzPrzejazdu':
        cur.execute("UPDATE Kurs SET komentarzPrzejazdu = ? WHERE idKurs = ?",(val,id)) 
    if col=='lacznaOplata':
        cur.execute("UPDATE Kurs SET lacznaOplata = ? WHERE idKurs = ?",(val,id))             
    con.commit()
    return redirect(url_for("tabela_kurs"))   
kurs_array = kurs_show()

#HISTORIA
def historia_show():
    cur.execute("""
        SELECT * FROM Historia
    """)
    row = cur.fetchone()
    names = row.keys()
    naglowek = []
    for row in names:
        naglowek.append(row)
    naglowek=tuple(i for i in naglowek)                               
    cur.execute("""
        SELECT * FROM Historia
    """)
    osoby = cur.fetchall()
    rekordy=[]
    rekordy.append(naglowek)    
    for row in osoby:
       rekordy.append(tuple(row))
    return np.array(rekordy)
def historia_insert(marka,model,ilM,cZK):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    cur.execute('INSERT INTO Historia VALUES(NULL, ?, ?,?,?)', (marka,model,ilM,cZK))
    con.commit()
    return redirect(url_for("tabela_historia"))
def historia_del(id):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    cur.execute('DELETE FROM Historia WHERE idHistoria= ? ',(id,))
    con.commit()
    return redirect(url_for("tabela_historia"))
def historia_alter(id,col,val):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    if col=='idKurs':
        cur.execute("UPDATE Historia SET idKurs = ? WHERE idHistoria = ?",(val,id))
    if col=='idKierowca':
        cur.execute("UPDATE Historia SET idKierowca = ? WHERE idHistoria = ?",(val,id))
    if col=='idKlient':
        cur.execute("UPDATE Historia SET idKlient = ? WHERE idHistoria = ?",(val,id))
    if col=='opis':
        cur.execute("UPDATE Historia SET opis = ? WHERE idHistoria = ?",(val,id))
    con.commit()
    return redirect(url_for("tabela_historia"))   
historia_array = historia_show()

# WIDOK MNIEJNIZ20
def widok_mniejniz20_show():
    cur.execute("""
        SELECT * FROM mniejNiz20
    """)
    row = cur.fetchone()
    names = row.keys()
    naglowek = []
    for row in names:
        naglowek.append(row)
    naglowek=tuple(i for i in naglowek)                               
    cur.execute("""
        SELECT * FROM mniejNiz20
    """)
    osoby = cur.fetchall()
    rekordy=[]
    rekordy.append(naglowek)    
    for row in osoby:
        rekordy.append(tuple(row))
    return np.array(rekordy)
widok_mniejniz20_array = widok_mniejniz20_show()

#WIDOK DOSTEPNI
def widok_dostepni_show():
    cur.execute("""
        SELECT * FROM dostepni
    """)
    row = cur.fetchone()
    names = row.keys()
    naglowek = []
    for row in names:
        naglowek.append(row)
    naglowek=tuple(i for i in naglowek)                               
    cur.execute("""
        SELECT * FROM dostepni
    """)
    osoby = cur.fetchall()
    rekordy=[]
    rekordy.append(naglowek)    
    for row in osoby:
        rekordy.append(tuple(row))
    return np.array(rekordy)
widok_dostepni_array = widok_dostepni_show()

#WIDOK NIEBIESKIESAM
def widok_niebieskiesam_show():
    cur.execute("""
        SELECT * FROM niebieskieSam
    """)
    row = cur.fetchone()
    names = row.keys()
    naglowek = []
    for row in names:
        naglowek.append(row)
    naglowek=tuple(i for i in naglowek)                               
    cur.execute("""
        SELECT * FROM niebieskieSam
    """)
    osoby = cur.fetchall()
    rekordy=[]
    rekordy.append(naglowek)    
    for row in osoby:
        rekordy.append(tuple(row))
    return np.array(rekordy)
widok_niebieskiesam_array = widok_niebieskiesam_show()



@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/tabele')
def tabele_all():
    return render_template('tabele_all.html')
 
@app.route('/tabele/adres', methods=['POST', 'GET'])
def tabela_adres():
    if request.method == 'POST':
        
        a = request.form.get(adres_array[0][1])
        b = request.form.get(adres_array[0][2])
        c = request.form.get(adres_array[0][3])
        d = request.form.get(adres_array[0][4])
        e = request.form.get(adres_array[0][5])
        delete = request.form.get('idDel')
        idAlt = request.form.get('idAlter')
        colAlt = request.form.get('colAlter')
        valAlt = request.form.get('valAlter')
        '''
        idAlt = request.form.get('alt'+adres_array[0][0])
        aAlt = request.form.get('alt'+adres_array[0][1])
        bAlt = request.form.get('alt'+adres_array[0][2])
        cAlt = request.form.get('alt'+adres_array[0][3])
        dAlt = request.form.get('alt'+adres_array[0][4])
        eAlt = request.form.get('alt'+adres_array[0][5])
        '''
        
        if a!=None and b!=None and c!=None and d!=None and e!=None:
            return adres_insert(a,b,c,d,e)
        elif delete !=None:
            #print("Usuwam id = "+str(delete))
            return adres_del(delete)
        elif idAlt!=None and colAlt!=None and valAlt!=None:
            return adres_alter(idAlt,colAlt,valAlt)
    else:
            return render_template('tabele_single.html', dane = adres_array, name = table_names[0])

@app.route('/tabele/znizka', methods=['POST', 'GET'])
def tabela_znizka():
    if request.method == 'POST':
        
        a = request.form.get(znizka_array[0][1])
        b = request.form.get(znizka_array[0][2])
        delete = request.form.get('idDel')
        idAlt = request.form.get('idAlter')
        colAlt = request.form.get('colAlter')
        valAlt = request.form.get('valAlter')
        
        if a!=None and b!=None:
            return znizka_insert(a,b)
        elif delete !=None:
            return znizka_del(delete)
        elif idAlt!=None and colAlt!=None and valAlt!=None:
            return znizka_alter(idAlt,colAlt,valAlt)
    else:
        return render_template('tabele_single.html', dane = znizka_array, name = table_names[1])
    
@app.route('/tabele/ocena', methods=['POST', 'GET'])
def tabela_ocena():
    if request.method == 'POST':
        
        a = request.form.get(ocena_array[0][1])
        b = request.form.get(ocena_array[0][2])
        delete = request.form.get('idDel')
        idAlt = request.form.get('idAlter')
        colAlt = request.form.get('colAlter')
        valAlt = request.form.get('valAlter')
        
        if a!=None and b!=None:
            return ocena_insert(a,b)
        elif delete !=None:
            return ocena_del(delete)
        elif idAlt!=None and colAlt!=None and valAlt!=None:
            return ocena_alter(idAlt,colAlt,valAlt)
    else:
        return render_template('tabele_single.html', dane = ocena_array, name = table_names[2])

@app.route('/tabele/klient', methods=['POST', 'GET'])
def tabela_klient():
    if request.method == 'POST':
        
        a = request.form.get(klient_array[0][1])
        b = request.form.get(klient_array[0][2])
        c = request.form.get(klient_array[0][3])
        d = request.form.get(klient_array[0][4])
        e = request.form.get(klient_array[0][5])
        f = request.form.get(klient_array[0][6])
        g = request.form.get(klient_array[0][7])
        delete = request.form.get('idDel')
        idAlt = request.form.get('idAlter')
        colAlt = request.form.get('colAlter')
        valAlt = request.form.get('valAlter')
        
        if a!=None and b!=None and c!=None and d!=None and e!=None and f!=None and g!=None:
            return klient_insert(a,b,c,d,e,f,g)
        elif delete !=None:
            return klient_del(delete)
        elif idAlt!=None and colAlt!=None and valAlt!=None:
            return klient_alter(idAlt,colAlt,valAlt)
    else:
        return render_template('tabele_single.html', dane = klient_array, name = table_names[3])

@app.route('/tabele/kierowca', methods=['POST', 'GET'])
def tabela_kierowca():
    if request.method == 'POST':
        
        a = request.form.get(kierowca_array[0][1])
        b = request.form.get(kierowca_array[0][2])
        c = request.form.get(kierowca_array[0][3])
        d = request.form.get(kierowca_array[0][4])
        e = request.form.get(kierowca_array[0][5])
        f = request.form.get(kierowca_array[0][6])
        g = request.form.get(kierowca_array[0][7])
        delete = request.form.get('idDel')
        idAlt = request.form.get('idAlter')
        colAlt = request.form.get('colAlter')
        valAlt = request.form.get('valAlter')
        
        if a!=None and b!=None and c!=None and d!=None and e!=None and f!=None and g!=None:
            return kierowca_insert(a,b,c,d,e,f,g)
        elif delete !=None:
            return kierowca_del(delete)
        elif idAlt!=None and colAlt!=None and valAlt!=None:
            return kierowca_alter(idAlt,colAlt,valAlt)
    else:
        return render_template('tabele_single.html', dane = kierowca_array, name = table_names[4])

@app.route('/tabele/rodzaj_samochodu', methods=['POST', 'GET'])
def tabela_rodzsam():
    if request.method == 'POST':
        
        a = request.form.get(rodzsam_array[0][1])
        b = request.form.get(rodzsam_array[0][2])
        c = request.form.get(rodzsam_array[0][3])
        d = request.form.get(rodzsam_array[0][4])
        delete = request.form.get('idDel')
        idAlt = request.form.get('idAlter')
        colAlt = request.form.get('colAlter')
        valAlt = request.form.get('valAlter')
        
        if a!=None and b!=None and c!=None and d!=None:
            return rodzsam_insert(a,b,c,d)
        elif delete !=None:
            return rodzsam_del(delete)
        elif idAlt!=None and colAlt!=None and valAlt!=None:
            return rodzsam_alter(idAlt,colAlt,valAlt)
    else:
        return render_template('tabele_single.html', dane = rodzsam_array, name = table_names[5])

@app.route('/tabele/egzemplarz', methods=['POST', 'GET'])
def tabela_egzemplarz():
    if request.method == 'POST':
        
        a = request.form.get(egzemplarz_array[0][1])
        b = request.form.get(egzemplarz_array[0][2])
        c = request.form.get(egzemplarz_array[0][3])
        d = request.form.get(egzemplarz_array[0][4])
        e = request.form.get(egzemplarz_array[0][5])
        delete = request.form.get('idDel')
        idAlt = request.form.get('idAlter')
        colAlt = request.form.get('colAlter')
        valAlt = request.form.get('valAlter')
        
        if a!=None and b!=None and c!=None and d!=None and e!=None:
            return egzemplarz_insert(a,b,c,d,e)
        elif delete !=None:
            return egzemplarz_del(delete)
        elif idAlt!=None and colAlt!=None and valAlt!=None:
            return egzemplarz_alter(idAlt,colAlt,valAlt)
    else:
        return render_template('tabele_single.html', dane = egzemplarz_array, name = table_names[6])

@app.route('/tabele/oplata', methods=['POST', 'GET'])
def tabela_oplata():
    if request.method == 'POST':
        
        a = request.form.get(oplata_array[0][1])
        b = request.form.get(oplata_array[0][2])
        delete = request.form.get('idDel')
        idAlt = request.form.get('idAlter')
        colAlt = request.form.get('colAlter')
        valAlt = request.form.get('valAlter')
        
        if a!=None and b!=None:
            return oplata_insert(a,b)
        elif delete !=None:
            return oplata_del(delete)
        elif idAlt!=None and colAlt!=None and valAlt!=None:
            return oplata_alter(idAlt,colAlt,valAlt)
    else:
        return render_template('tabele_single.html', dane = oplata_array, name = table_names[7])

@app.route('/tabele/taryfa', methods=['POST', 'GET'])
def tabela_taryfa():
    if request.method == 'POST':
        
        a = request.form.get(taryfa_array[0][1])
        b = request.form.get(taryfa_array[0][2])
        delete = request.form.get('idDel')
        idAlt = request.form.get('idAlter')
        colAlt = request.form.get('colAlter')
        valAlt = request.form.get('valAlter')
        
        if a!=None and b!=None:
            return taryfa_insert(a,b)
        elif delete !=None:
            return taryfa_del(delete)
        elif idAlt!=None and colAlt!=None and valAlt!=None:
            return taryfa_alter(idAlt,colAlt,valAlt)
    else:
        return render_template('tabele_single.html', dane = taryfa_array, name = table_names[8])

@app.route('/tabele/kurs', methods=['POST', 'GET'])
def tabela_kurs():
    if request.method == 'POST':
        
        a = request.form.get(kurs_array[0][1])
        b = request.form.get(kurs_array[0][2])
        c = request.form.get(kurs_array[0][3])
        d = request.form.get(kurs_array[0][4])
        e = request.form.get(kurs_array[0][5])
        f = request.form.get(kurs_array[0][6])
        g = request.form.get(kurs_array[0][7])
        h = request.form.get(kurs_array[0][8])
        i = request.form.get(kurs_array[0][9])
        j = request.form.get(kurs_array[0][10])
        k = request.form.get(kurs_array[0][11])
        l = request.form.get(kurs_array[0][12])
        delete = request.form.get('idDel')
        idAlt = request.form.get('idAlter')
        colAlt = request.form.get('colAlter')
        valAlt = request.form.get('valAlter')
        
        if a!=None and b!=None and c!=None and d!=None and e!=None and f!=None and g!=None and h!=None and i!=None and j!=None and k!=None and l!=None:
            return kurs_insert(a,b,c,d,e,f,gh,i,j,k,l)
        elif delete !=None:
            return kurs_del(delete)
        elif idAlt!=None and colAlt!=None and valAlt!=None:
            return kurs_alter(idAlt,colAlt,valAlt)
    else:
        return render_template('tabele_single.html', dane = kurs_array, name = table_names[9])

@app.route('/tabele/historia', methods=['POST', 'GET'])
def tabela_historia():
    if request.method == 'POST':
        
        a = request.form.get(historia_array[0][1])
        b = request.form.get(historia_array[0][2])
        c = request.form.get(historia_array[0][3])
        d = request.form.get(historia_array[0][4])
        delete = request.form.get('idDel')
        idAlt = request.form.get('idAlter')
        colAlt = request.form.get('colAlter')
        valAlt = request.form.get('valAlter')
        
        if a!=None and b!=None and c!=None and d!=None:
            return historia_insert(a,b,c,d,e)
        elif delete !=None:
            return historia_del(delete)
        elif idAlt!=None and colAlt!=None and valAlt!=None:
            return historia_alter(idAlt,colAlt,valAlt)
    else:
        return render_template('tabele_single.html', dane = historia_array, name = table_names[10])

@app.route('/widoki')
def widoki_all():
    return render_template('widoki_all.html')

@app.route('/widoki/widok_mniejniz20')
def widok_mniejniz20():
    return render_template('widoki_single.html', dane = widok_mniejniz20_array, name = view_names[0][0])

@app.route('/widoki/widok_dostepni')
def widok_dostepni():
    return render_template('widoki_single.html', dane = widok_dostepni_array, name = view_names[1][0])

@app.route('/widoki/widok_niebieskiesam')
def widok_niebieskiesam():
    return render_template('widoki_single.html', dane = widok_niebieskiesam_array, name = view_names[2][0])
    
    
if __name__ == '__main__':
    app.run(debug=True)   

con.close()  

