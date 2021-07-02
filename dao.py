from domain import Product
import psycopg2 as pg
from my_configuration import connection_kwargs



def get_products():
    wynik=[]
    with pg.connect(**connection_kwargs) as connection:
    #with pg.connect(host="localhost", port=5432, database="szkolenie", user="szkolenie", password="jsystems" ) as connection:
        cursor=connection.cursor()
        cursor.execute('select * from produkty order by cena_produktu desc')
        for w in cursor:
            p=Product(w[0],w[1],w[2],w[3])
            wynik.append(p)
    return wynik

def get_product(id):
    with pg.connect(**connection_kwargs) as connection:
    # with pg.connect(host="localhost", port=5432, database="szkolenie", user="szkolenie", password="jsystems" ) as connection:
        cursor=connection.cursor()
        cursor.execute(f"select * from produkty where id_produktu={id}")
        w=cursor.fetchone()
        product=Product(w[0],w[1],w[2],w[3])
    return product

# p=get_product(1)
# print(p.product_id,p.product_name,p.product_price)

def save_product(p):
    with pg.connect(**connection_kwargs) as connection:
        cursor=connection.cursor()
        cursor.execute(f"insert into produkty(nazwa_produktu,opis_produktu,cena_produktu) values ('{p.product_name}','{p.product_description}',{p.product_price})")
        connection.commit()

print(connection_kwargs)
for k in connection_kwargs:
    print(k,connection_kwargs[k])