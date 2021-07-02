from domain import Product
import psycopg2 as pg
connection_kwargs={
    "host": "localhost",
    "port":5432,
    "database": "szkolenie",
    "user": "szkolenie",
    "password": "jsystems"
}

def get_products_fake():
    wynik = []
    wynik.append(Product(1, "Bubulator", 123))
    wynik.append(Product(2, "Wihajster", 542))
    wynik.append(Product(3, "Pykadło", 870))
    wynik.append(Product(4, "Tenteges", 120))
    return wynik

def get_products():
    wynik=[]
    with pg.connect(**connection_kwargs) as connection:
    #with pg.connect(host="localhost", port=5432, database="szkolenie", user="szkolenie", password="jsystems" ) as connection:
        cursor=connection.cursor()
        cursor.execute('select id_produktu,nazwa_produktu,cena_produktu from produkty order by cena_produktu desc')
        for w in cursor:
            p=Product(w[0],w[1],w[2])
            wynik.append(p)
    return wynik

def get_product(id):
    with pg.connect(**connection_kwargs) as connection:
    # with pg.connect(host="localhost", port=5432, database="szkolenie", user="szkolenie", password="jsystems" ) as connection:
        cursor=connection.cursor()
        cursor.execute(f"select id_produktu,nazwa_produktu,cena_produktu from produkty where id_produktu={id}")
        w=cursor.fetchone()
        product=Product(w[0],w[1],w[2])
    return product

# p=get_product(1)
# print(p.product_id,p.product_name,p.product_price)

print(connection_kwargs)
for k in connection_kwargs:
    print(k,connection_kwargs[k])