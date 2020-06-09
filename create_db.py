#!/usr/bin/env python
# coding: utf-8

# # Laboratoria 11

# # Zadanie 6

# In[1]:


import sqlite3
import pandas as pd
import os.path
from os import path

work_path='C:\\Users\\matij\\Documents\\STUDIA\\Semestr 4 (xml,Java+SQL)\\Aplikacje bazodanowe\\venv\\lab13_projekt2\\'
curr_path=os.chdir(work_path)

con = sqlite3.connect('baza.db')
cur = con.cursor()


# ## Tabela 'Adres'

# In[2]:


cur.executescript("""
    DROP TABLE IF EXISTS Adres;
    CREATE TABLE Adres (
        idAdres INTEGER PRIMARY KEY,
        miejscowosc VARCHAR(30) NOT NULL,
        ulica VARCHAR(50) NOT NULL,
        nr_domu VARCHAR(10) NOT NULL,
        nr_mieszkania INTEGER,
        kod CHAR(11) NOT NULL
    )""")

con.commit()


# In[3]:


records = (
    ('Koszalin','krawiecka', 12, 4,'60-323'),
    ('Kraków','stanisławska', 10, 5,'80-549'),
    ('Bytom','piekarniana', 5, 5,'93-543'),
    ('Bydgoszcz','dąbrowszczaków', 23, 8,'43-432'),
    ('Morąg','krynicka', 44, 9,'87-654')
)

cur.executemany('INSERT INTO Adres VALUES(NULL, ?, ?, ?, ?, ?)', records)
con.commit()


# In[4]:


cur.execute("SELECT * FROM Adres;")
column_names = [tupla[0] for tupla in cur.description]
data = cur.fetchall()
column_names = tuple(i for i in column_names)

dfAdres = pd.DataFrame(data, columns = column_names)
dfAdres


# ## Tabela 'Znizka'

# In[5]:


cur.executescript("""
    DROP TABLE IF EXISTS Znizka;
    CREATE TABLE Znizka (
        idZnizka INTEGER PRIMARY KEY,
        nazwa VARCHAR(30) NOT NULL,
        procentRabatu INT NOT NULL CHECK(procentRabatu<=100)
    )""")

con.commit()


# In[6]:


records = (
    ('Studencka', 51),
    ('Seniorska' , 51),
    ('Szkolna', 23 ),
    ('Dla polityków',100),
    ('Dla weteranów', 100)
)

cur.executemany('INSERT INTO Znizka VALUES(NULL, ?, ?)', records)
con.commit()


# In[7]:


cur.execute("SELECT * FROM Znizka;")
column_names = [tupla[0] for tupla in cur.description]
data = cur.fetchall()
column_names = tuple(i for i in column_names)

dfZnizka = pd.DataFrame(data, columns = column_names)
dfZnizka


# ## Tabela 'Ocena'

# In[8]:


cur.executescript("""
    DROP TABLE IF EXISTS Ocena;
    CREATE TABLE Ocena (
        idOcena INTEGER PRIMARY KEY,
        ocenaKierowcy DECIMAL(3,2) NOT NULL DEFAULT 0.00 CHECK(ocenaKierowcy<=5.00),
        podwyzkaProcent INT NOT NULL CHECK(podwyzkaProcent<=100)
    )""")

con.commit()


# In[9]:


records = (
    (5.0 , 30),
    (4.5 , 25),
    (4.0 , 20),
    (3.5, 15),
    (3.0 , 0)
)

cur.executemany('INSERT INTO Ocena VALUES(NULL, ?, ?)', records)
con.commit()


# In[10]:


cur.execute("SELECT * FROM Ocena;")
column_names = [tupla[0] for tupla in cur.description]
data = cur.fetchall()
column_names = tuple(i for i in column_names)

dfOcena = pd.DataFrame(data, columns = column_names)
dfOcena


# ## Tabela 'Klient'

# In[11]:


cur.executescript("""
    DROP TABLE IF EXISTS Klient;
    CREATE TABLE Klient (
        idKlient INTEGER PRIMARY KEY,
        Adres3 INTEGER REFERENCES Adres(idAdres),
        Adres2 INTEGER REFERENCES Adres(idAdres),
        Adres1 INTEGER REFERENCES Adres(idAdres),
        idZnizka INTEGER REFERENCES Znizka(idZnizka),
        imie VARCHAR(30) NOT NULL,
        nazwisko VARCHAR(30) NOT NULL,
        dataUrodzenia DATE NOT NULL
    )""")

con.commit()


# In[12]:


records = (
    (1,3, None, 2, 'Kamil','Łukaszczyk', '2003-10-11'),
    (2,1, 2, 3, 'Pawel','Dąbrowszczak', '1990-12-03'),
    (4,4,3,1, 'Tomasz', 'Prawda', '1963-05-03'),
    (1, 2, 2, None, 'Karol', 'Niezgoda', '1999-05-12'),
    (3,1,2, None, 'Stefan','Paprotka', '1997-02-01')
)

cur.executemany('INSERT INTO Klient VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)', records)
con.commit()


# In[13]:


cur.execute("SELECT * FROM Klient;")
column_names = [tupla[0] for tupla in cur.description]
data = cur.fetchall()
column_names = tuple(i for i in column_names)

dfKlient = pd.DataFrame(data, columns = column_names)
dfKlient


# ## Tabela 'Kierowca'

# In[14]:


cur.executescript("""
    DROP TABLE IF EXISTS Kierowca;
    CREATE TABLE Kierowca (
        idKierowca INTEGER PRIMARY KEY,
        idOcena INTEGER NOT NULL REFERENCES  Ocena(idOcena),
        adresTymcz INTEGER REFERENCES Adres(idAdres),
        adresStaly INTEGER NOT NULL REFERENCES Adres(idAdres),
        adresKorespondencji INTEGER NOT NULL REFERENCES Adres(idAdres),
        imie VARCHAR(30) NOT NULL,
        nazwisko VARCHAR(30) NOT NULL,
        czyDostepny BIT NOT NULL
    )""")

con.commit()


# In[15]:


records = (
    (1,2,3,4,'Wojtek', 'Marchewa',0),
    (4,3,2,1,'Mateusz', 'Dymbała',1),
    (2,3,1,4,'Dominik', 'Kapustnik',1),
    (1,3,3,2,'Darek', 'Kulak',0),
    (3,4,1,2,'Mikołaj', 'Orzeł',1),
    (5,1,3,2,'Mateusz', 'Kowalski',0)
)

cur.executemany('INSERT INTO Kierowca VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)', records)
con.commit()


# In[16]:


cur.execute("SELECT * FROM Kierowca;")
column_names = [tupla[0] for tupla in cur.description]
data = cur.fetchall()
column_names = tuple(i for i in column_names)

dfKierowca = pd.DataFrame(data, columns = column_names)
dfKierowca


# ## Tabela 'Rodzaj_samochodu'

# In[17]:


cur.executescript("""
    DROP TABLE IF EXISTS Rodzaj_samochodu;
    CREATE TABLE Rodzaj_samochodu (
        idRodzaj_samochodu INTEGER PRIMARY KEY,
        marka VARCHAR(30) NOT NULL,
        model VARCHAR(30) NOT NULL,
        iloscMiejsc INT NOT NULL,
        cenaZaKm DECIMAL(4,2) NOT NULL
    )""")

con.commit()


# In[18]:


records = (
    ('toyota', 'corolla',5, 2.30),
    ('volkswagen', 'beetle',5, 1.50),
    ('ford', 'f-series',5, 1.80),
    ('honda', 'acord',5, 3.20),
    ('honda', 'civic',5, 5.50)
)

cur.executemany('INSERT INTO Rodzaj_samochodu VALUES(NULL, ?, ?, ?, ?)', records)
con.commit()


# In[19]:


cur.execute("SELECT * FROM Rodzaj_samochodu;")
column_names = [tupla[0] for tupla in cur.description]
data = cur.fetchall()
column_names = tuple(i for i in column_names)

dfRodzaj_samochodu = pd.DataFrame(data, columns = column_names)
dfRodzaj_samochodu


# ## Tabela 'Egzemplarz'

# In[20]:


cur.executescript("""
    DROP TABLE IF EXISTS Egzemplarz;
    CREATE TABLE Egzemplarz (
        idKierowca INTEGER NOT NULL REFERENCES Kierowca(idKierowca),
        idRodzaj_samochodu INTEGER NOT NULL REFERENCES Rodzaj_samochodu(idRodzaj_samochodu),
        unikalnyNr INTEGER NOT NULL UNIQUE CHECK(unikalnyNr<1000),
        kolor VARCHAR(30) NOT NULL,
        ocenaSamoch DECIMAL(3,2) NOT NULL DEFAULT 0.00 CHECK(ocenaSamoch<=5.00),
        PRIMARY KEY (idKierowca,idRodzaj_samochodu)
    )""")

con.commit()


# In[21]:


records = (
    (2,5,512,'niebieski',3.79),
    (3,1,356,'czerwony',4.89),
    (1,2,198,'zolty',3.66),
    (5,3,25,'niebieski',4.55),
    (4,4,199,'czarny',4.65)
)

cur.executemany('INSERT INTO Egzemplarz VALUES(?, ?, ?, ?, ?)', records)
con.commit()


# In[22]:


cur.execute("SELECT * FROM Egzemplarz;")
column_names = [tupla[0] for tupla in cur.description]
data = cur.fetchall()
column_names = tuple(i for i in column_names)

dfEgzemplarz = pd.DataFrame(data, columns = column_names)
dfEgzemplarz


# ## Tabela 'Oplata'

# In[23]:


cur.executescript("""
    DROP TABLE IF EXISTS Oplata;
    CREATE TABLE Oplata (
        idOplata INTEGER PRIMARY KEY,
        formaPlatnosci VARCHAR(30) NOT NULL,
        oplataDodatk DECIMAL(3,2) NOT NULL
    )""")

con.commit()


# In[24]:


records = (
    ('Karta debetowa',0.00),
    ('Karta kredytowa',0.00),
    ('PayPal',0.00),
    ('Gotowka',5.00),
    ('PaySafeCard',2.50)
)

cur.executemany('INSERT INTO Oplata VALUES(NULL, ?, ?)', records)
con.commit()


# In[25]:


cur.execute("SELECT * FROM Oplata;")
column_names = [tupla[0] for tupla in cur.description]
data = cur.fetchall()
column_names = tuple(i for i in column_names)

dfOplata = pd.DataFrame(data, columns = column_names)
dfOplata


# ## Tabela 'Taryfa'

# In[26]:


cur.executescript("""
    DROP TABLE IF EXISTS Taryfa;
    CREATE TABLE Taryfa (
        idTaryfa INTEGER PRIMARY KEY,
        nazwa VARCHAR(30) NOT NULL,
        wysokoscTaryfy DECIMAL(4,2) NOT NULL
    )""")

con.commit()


# In[27]:


records = (
    ('nocna',3.50),
    ('weekendowa',5.50),
    ('zwykla',0.00),
    ('dodatkowy bagaz',8.20),
    ('zwierze domowe',10.50)
)

cur.executemany('INSERT INTO Taryfa VALUES(NULL, ?, ?)', records)
con.commit()


# In[28]:


cur.execute("SELECT * FROM Taryfa;")
column_names = [tupla[0] for tupla in cur.description]
data = cur.fetchall()
column_names = tuple(i for i in column_names)

dfTaryfa = pd.DataFrame(data, columns = column_names)
dfTaryfa


# ## Tabela 'Kurs'

# In[29]:


cur.executescript("""
    DROP TABLE IF EXISTS Kurs;
    CREATE TABLE Kurs (
        idKurs INTEGER PRIMARY KEY,
        idOplata INTEGER NOT NULL REFERENCES Oplata(idOplata),
        idTaryfa INTEGER NOT NULL REFERENCES Taryfa(idTaryfa),
        idKierowca INTEGER NOT NULL REFERENCES Kierowca(idKierowca),
        idKlient INTEGER NOT NULL REFERENCES Klient(idKlient),
        lokalizacjaKonc INTEGER NOT NULL REFERENCES Adres(idAdres),
        lokalizacjaPocz INTEGER NOT NULL REFERENCES Adres(idAdres),
        dataKursu DATE NOT NULL,
        godzinaPocz TIME(0)NOT NULL,
        godzinaKonc TIME(0) NOT NULL,
        ocenaPrzejazdu DECIMAL(3,2) NOT NULL,
        komentarzPrzejazdu VARCHAR(200),
        lacznaOplata DECIMAL(19,2) NOT NULL
    )""")

con.commit()


# In[30]:


records = (
    (2,3,4,1,4,5,'2019-02-14','16:24:35','16:39:35',5.00,'Wszystko ok',13.50),
    (4,1,2,3,5,4,'2019-04-11','12:54:15','13:13:39',3.50,'Malo rozmowny kierowca',20.10),
    (1,5,4,2,2,1,'2019-10-25','20:28:15','20:39:31',4.50,None,15.90),
    (5,1,1,4,3,5,'2019-12-14','09:28:31','10:02:20',2.50,'Kierowca pomylil droge',25.50),
    (2,1,2,5,3,1,'2019-12-24','21:23:30','21:30:24',5.00,'Szybki transport',13.00)
)

cur.executemany('INSERT INTO Kurs VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', records)
con.commit()


# In[31]:


cur.execute("SELECT * FROM Kurs;")
column_names = [tupla[0] for tupla in cur.description]
data = cur.fetchall()
column_names = tuple(i for i in column_names)

dfKurs = pd.DataFrame(data, columns = column_names)
dfKurs


# ## Tabela 'Historia'

# In[32]:


cur.executescript("""
    DROP TABLE IF EXISTS Historia;
    CREATE TABLE Historia (
        idHistoria INTEGER PRIMARY KEY,
        idKurs INTEGER NOT NULL REFERENCES Kurs(idKurs),
        idKierowca INTEGER NOT NULL REFERENCES Kierowca(idKierowca),
        idKlient INTEGER NOT NULL REFERENCES Klient(idKlient),
        opis VARCHAR (500)
    )""")

con.commit()


# In[33]:


records = (
    (2,2,3,'Neutralny'),
    (1,4,1,'Pozytywny'),
    (3,1,4,'Pozytywny'),
    (5,2,5,'Pozytywny'),
    (4,1,4,'Zwrot')
)

cur.executemany('INSERT INTO Historia VALUES(NULL, ?, ?, ?, ?)', records)
con.commit()


# In[34]:


cur.execute("SELECT * FROM Historia;")
column_names = [tupla[0] for tupla in cur.description]
data = cur.fetchall()
column_names = tuple(i for i in column_names)

dfHistoria = pd.DataFrame(data, columns = column_names)
dfHistoria


# # Zadanie 7

# ### widok 1 - mniejNiz20 - widok użytkowników, którzy zapłacili za ostatni kurs mniej niż 20 zł.

# In[35]:


cur.executescript("""
    DROP VIEW IF EXISTS mniejNiz20;
    CREATE VIEW mniejNiz20 AS
    SELECT k.idKlient,k.imie, k.nazwisko, k.dataUrodzenia, ku.lacznaOplata,
    COALESCE(ku.komentarzPrzejazdu,'brak komentarza') AS 'komentarzPrzejazdu', ke.imie
    AS 'imieKierowcy', ke.nazwisko AS 'nazwiskoKierowcy',a.miejscowosc AS 'lokPocz', ad.miejscowosc AS 'lokKonc'
    FROM Klient k JOIN Kurs ku ON k.idKlient=ku.idKlient
    JOIN Kierowca ke ON ku.idKierowca=ke.idKierowca
    JOIN Adres a ON a.idAdres=ku.lokalizacjaPocz JOIN Adres ad ON ad.idAdres=ku.lokalizacjaKonc
    GROUP BY k.idKlient,k.nazwisko, k.imie, k.dataUrodzenia, ku.lacznaOplata, ku.komentarzPrzejazdu, ke.imie, ke.nazwisko, a.miejscowosc, ad.miejscowosc
    HAVING ku.lacznaOplata<20.00;
""")

con.commit()

cur.execute("""
    SELECT * FROM mniejNiz20
    """)
view_temp = cur.fetchall()
column_names = [tupla[0] for tupla in cur.description]
column_names = tuple(i for i in column_names)

mniejNiz20 = pd.DataFrame(view_temp, columns = column_names)
mniejNiz20


# ### widok 2 - dostepni - widok dostępnych kierowców

# In[36]:


cur.executescript("""
    DROP VIEW IF EXISTS dostepni;
    CREATE VIEW dostepni AS
    SELECT k.idKierowca, k.imie, k.nazwisko, o.ocenaKierowcy, s.marka, s.model,
    s.iloscMiejsc
    FROM Kierowca k JOIN Ocena o ON k.idOcena=o.idOcena
    JOIN Egzemplarz e ON k.idKierowca=e.idKierowca
    JOIN Rodzaj_samochodu s ON e.idRodzaj_samochodu=s.idRodzaj_samochodu
    WHERE K.czyDostepny=1;
""")

con.commit()

cur.execute("""
    SELECT * FROM dostepni
    """)
view_temp = cur.fetchall()
column_names = [tupla[0] for tupla in cur.description]
column_names = tuple(i for i in column_names)

dostepni = pd.DataFrame(view_temp, columns = column_names)
dostepni


# ### widok 3 - niebieskieSam - widok kursów, w których kierowca prowadził niebieski samochód

# In[37]:


cur.executescript("""
    DROP VIEW IF EXISTS niebieskieSam;
    CREATE VIEW niebieskieSam AS
    SELECT kur.idKurs, kl.idKlient, kl.imie AS 'imieKlienta', kl.nazwisko AS 'nazwiskoKlienta', 
    kier.idKierowca, kier.imie AS 'imieKierowcy', kier.nazwisko AS 'nazwiskoKierowcy', kur.lacznaOplata, 
    kur.ocenaPrzejazdu, s.marka, s.model, e.kolor
    FROM Kurs kur JOIN Klient kl ON kur.idKlient=kl.idKlient
    JOIN Kierowca kier ON kur.idKierowca=kier.idKierowca
    JOIN Egzemplarz e ON kier.idKierowca=e.idKierowca
    JOIN Rodzaj_samochodu s ON e.idRodzaj_samochodu=s.idRodzaj_samochodu
    WHERE e.kolor='niebieski';
""")

con.commit()

cur.execute("""
    SELECT * FROM niebieskieSam
    """)
view_temp = cur.fetchall()
column_names = [tupla[0] for tupla in cur.description]
column_names = tuple(i for i in column_names)

niebieskieSam = pd.DataFrame(view_temp, columns = column_names)
niebieskieSam


# ### wszystkie widoki w bazie

# In[38]:


#cur.execute("SELECT name FROM sqlite_master WHERE type='view';")
#print(cur.fetchall())


# # Zadanie 8

# ### funkcja 1 - jakaPrzyslugujeZnizka - jest to funkcja, która zwraca rodzaj zniżki przypisanej do danego klienta. Do funkcji podajemy imię i nazwisko klienta. Gdy użytkownikowi nie przysługuje żadna zniżka funkcja wypisze komunikat: “brak zniżki”. W przypadku braku użytkownika w bazie, funkcja wypisze “nie ma takiej osoby w bazie danych”

# In[39]:


def jakaPrzyslugujeZnizka(imie, nazwisko):
    params = (imie, nazwisko)
    func = ("""
    SELECT z.nazwa FROM Znizka z LEFT JOIN
    Klient k ON k.idZnizka=z.idZnizka WHERE k.imie=@imie AND
    k.nazwisko=@nazwisko
    """)
    
    cur.execute(func, params)
    final = cur.fetchall()
    
    check = ("""
    SELECT * FROM Klient WHERE imie=@imie AND nazwisko=@nazwisko
    """)
    
    cur.execute(check, params)
    exists = pd.DataFrame(cur.fetchall(),params)
    
    out = pd.DataFrame(final, columns = ['znizka'])
    
    if out.empty: out = 'BRAK ZNIŻKI'
    if exists.empty: out = 'NIE MA TAKIEJ OSOBY W BAZIE DANYCH'
    
    return out

#print(jakaPrzyslugujeZnizka('Pawel','Dąbrowszczak'))


# ### funkcja 2 - dostepnoscSamochodu - jest to funkcja, która powiadamia użytkownika o aktywnych samochodach o ocenie wyższej od podanej przez niego. Funkcja informuje także o kierowcy prowadzącym dany pojazd.

# In[40]:


def dostepnoscSamochodu(ocena):
    params = (ocena,)
    func = ("""
    SELECT rs.marka,rs.model,e.kolor,e.ocenaSamoch,rs.cenaZaKm,k.imie AS 'imieKierowcy',k.nazwisko AS 'nazwiskoKierowcy' 
    FROM Rodzaj_samochodu rs
    JOIN Egzemplarz e ON rs.idRodzaj_samochodu=e.idRodzaj_samochodu
    JOIN Kierowca k ON k.idKierowca=e.idKierowca WHERE e.ocenaSamoch>=@ocena AND k.czyDostepny=1
    """)
    cur.execute(func,params)
    final = cur.fetchall()
    
    column_names = [tupla[0] for tupla in cur.description]
    column_names = tuple(i for i in column_names)
    
    out = pd.DataFrame(final, columns = column_names)
    
    return out

#print(dostepnoscSamochodu(3.5))


# ### funkcja 3 - filtrMiejsc - jest to funkcja, która filtruje kierowców pod względem miejscowości adresu stałego, podanej przez użytkownika.

# In[41]:


def filtrMiejsc(m):
    params = (m,)
    func = ("""
    SELECT k.idKierowca, k.imie, k.nazwisko
    FROM Kierowca k JOIN Adres a ON k.adresStaly=a.idAdres
    WHERE @m=a.miejscowosc
        """)
    cur.execute(func, params)
    final = cur.fetchall()
    
    column_names = [tupla[0] for tupla in cur.description]
    column_names = tuple(i for i in column_names)
    
    out = pd.DataFrame(final, columns = column_names)
    
    return out
    

#print(filtrMiejsc('Bytom'))
                            


# In[42]:


con.close()

