from domain import Product
import psycopg2 as pg

def get_products_fake():
    wynik = []
    wynik.append(Product(1, "Bubulator", 123))
    wynik.append(Product(2, "Wihajster", 542))
    wynik.append(Product(3, "Pykadło", 870))
    wynik.append(Product(4, "Tenteges", 120))
    return wynik

def get_products():
    wynik=[]
    with pg.connect(host="localhost", port=5432, database="szkolenie", user="szkolenie", password="jsystems" ) as connection:
        cursor=connection.cursor()
        cursor.execute('select id_produktu,nazwa_produktu,cena_produktu from produkty order by cena_produktu desc')
        for w in cursor:
            p=Product(w[0],w[1],w[2])
            wynik.append(p)
    return wynik

def get_product(id):
    product=Product(1,"Fejkowy produkt",555)
    return product

