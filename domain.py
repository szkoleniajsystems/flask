class Author:
    imie=None
    nazwisko=None

    def __init__(self,i,n):
        self.imie=i
        self.nazwisko=n

class Product:
    product_id=None
    product_name=None
    product_description=None
    product_price=None
    def __init__(self,i,n,d,p):
        self.product_id=i
        self.product_name=n
        self.product_description=d
        self.product_price=p

