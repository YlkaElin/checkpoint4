import psycopg2
from config import config as config

# lisää toimipaikka Espoo astioille
def toimipaikka():
    con = None
    try:
        con = psycopg2.connect(**config())
        cur = con.cursor()
        SQL = "UPDATE astia SET toimipaikka_id = (SELECT toimipaikka.id FROM toimipaikka WHERE toimipaikka.id=1)"
        cur.execute(SQL)

        print(cur.rowcount, "record inserted.")

        con.commit()
        cur.close()
        con.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

# Päivitä lasien lkm 100
def paivita():
    con = None
    try:
        con = psycopg2.connect(**config())
        cur = con.cursor()
        SQL = "UPDATE astia SET lkm=100 WHERE nimi='Lasi';"
        cur.execute(SQL)

        print(cur.rowcount, "record inserted.")

        con.commit()
        cur.close()
        con.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()


#lisää kaikki toimipaikat 100 kpl --ei toimi, jäi kesken
def lisaa():
    con = None
    try:
        con = psycopg2.connect(**config())
        cur = con.cursor()
        SQL = "INSERT INTO astia (lkm,toimipaikka_id) VALUES(%s,%s);"
        val=(100,"SELECT toimipaikka.id FROM toimipaikka WHERE toimipaikka.id=2;")
        cur.execute(SQL, val)

        print(cur.rowcount, "record inserted.")

        con.commit()
        cur.close()
        con.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()




if __name__ == "__main__":
    #toimipaikka()
    #paivita()
    lisaa()