from domain import Product


def get_products():
    wynik = []
    wynik.append(Product(1, "Bubulator", 123))
    wynik.append(Product(2, "Wihajster", 542))
    wynik.append(Product(3, "Pykadło", 870))
    wynik.append(Product(4, "Tenteges", 120))
    return wynik
