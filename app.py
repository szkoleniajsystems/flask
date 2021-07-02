from flask import Flask,render_template
from domain import Author
from dao import get_products
app = Flask(__name__)

#*args
#**kwargs

@app.route('/')
def index():
    at=Author('Andrzej','Klusieiwcz')
    jezyki=['python','pl/sql','java','assembler','C#']
    return render_template("index.html",author=at, languages=jezyki,products=get_products())


@app.route('/product_details')
def product_details():
    return render_template("product_details.html")

# @app.route('/')
# def index():
#     return render_template("index.html",imie='Andrzej',nazwisko="Klusiewicz")

# @app.route('/')
# def index():
#     return '<h1>Siema Muppet!</h1>'


if __name__ == '__main__':
    app.run(debug=True,port=80)

#1. Stwórz nową aplikację, tak by miała włączony tryb debug oraz chodziła na porcie 8080.
#Do tej aplikacji dodaj 3 ekrany obsługujące 3 adresy:
# /
# /list
# /about
#każdy z tych ekranów powinien wyświetlać plik HTML z odpowiednim nagłówkiem

#przerwa do 14:37

#klusiewicz@jsystems.pl

#Do aplikacji Todos dodaj menu które będzie zawierało linki do wszystkich jej ekranów
#Tkinter

#Do aplikacji Todos dodaj klasę Author (w osobnym module) która będzie zawierała imię, nazwisko, email, url zdjęcia.
#Dodaj też moduł "dao.py" i umieść w nim funkcję get_author() która zwróci obiekt wraz z danymi. Dane o autorze
#maja byc uzupelniane wewnątrz funkcji get_author(). Odbierz w metodzie mapujacej adres /about obiekt klasy Author
#z naszego dao i przekaz do widoku. Na poziomie widoku wyswietl te dane w formie tabelarycznej.





#Do aplikacji ToDos dodaj klasę ToDo. Klasa ta ma posiadać: todo_id, todo_name,todo_description,priority
#Dodaj do dao funkcję get_todos() zwracającą listę jakichś fejkowych todos (ze 4 obiekty).
#Przekaż dane odebrane z funkcji get_todos() i wyświetl w tabeli w widoku /list

#statusy HTTP

#przerwa do 11:55


#zadbaj o to by na liście zadań nazwa zadania byla roznych kolorow w zaleznosci od priorytetu.
#zielony=1
#pomaranczowy=2
#czerwony=3



