import psycopg2
from config import config as config

# Lisää astioita tauluun
def lisaa_astiat():
    con = None
    try:
        con = psycopg2.connect(**config())
        cur = con.cursor()
        SQL = "INSERT INTO astia (nimi, lkm) VALUES (%s,%s);"
        val = ("Muki",100)
        val2 = ("Lasi", 80)
        val3 = ("Iso lautanen", 40)
        val4 = ("Pieni lautanen", 40)
        cur.execute(SQL, val)
        cur.execute(SQL, val2)
        cur.execute(SQL, val3)
        cur.execute(SQL, val4)
        print(cur.rowcount, "rivi(ä) lisätty.")
        con.commit()
        cur.close()
        con.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()


#Hakee astiat tietokannasta ja tulostaa haun tuloksen
def tulosta_astiat():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        sarakkeet = "nimi, lkm"
        taulu = "astia"
        SQL = (f"SELECT {sarakkeet} FROM {taulu};")
        cursor.execute(SQL)
        result = cursor.fetchall()

        for row in result:
            print(f"{row}kpl")    
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()


if __name__ == "__main__":
    #lisaa_astiat()
    tulosta_astiat()