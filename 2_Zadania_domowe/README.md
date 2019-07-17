<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Zaawansowane Django &ndash; praca domowa

## Dzień 1.

### Zadanie 0. 

W projekcie **3_Django** utwórz i skonfiguruj aplikację **homework**.

### Zadanie 1. 

Wyobraź sobie oprogramowanie sklepu internetowgo. Sklep może sprzedawać dowolny towar, zatem będzie potrzebna struktura danych dla towaru i kategorii. Każdy towar może posiadać wiele kategorii. Każda kategoria może zwierać wiele towarów. Kategorie mają być definiowane przez użytkownika, zatem muszą być przechowywane w bazie danych.

Zdefiniuj następujące modele: 

* `Category` a w nim następujące pola:
    * `category_name` string o max długości 64 znaki,
    * `slug` string o max długości 64 znaki, unikalny.

Slug to pole, które przechowuje identyfikator znakowy kategorii. Może zawierać tylko małe litery, cyfry i znak - zamiast spacji. Powinien być unikalny.

* `Product` czyli opis towaru, a w nim następujące pola:
    * `name`: nazwa towaru, string o max długości 128 znaków,
    * `description`: opis, string o nieograniczonej liczbie znaków,
    * `price`: cena netto towaru, liczba zmiennoprzecinkowa (zignorujmy niedoskonałości typu float),
    * `vat`: podatek VAT, może przyjmować wartości liczbowe: 0.23, 0.08, 0.05, 0,
    * `stock`: liczba produktów w magazynie, integer,
    * `categories`: relacja typu "wiele do wielu" między `Product`, a `Category`.

Wypełnij modele danymi: zdefiniuj kilka dowolnych kategorii, dodaj do kategorii kilka produktów.

### Zadanie 2.

* Zdefiniuj szablon bazowy, po którym dziedziczą wszystkie inne szablony w aplikacji, szablon powinien mieć nazwę `base.html`

* Napisz widok, który udostępnisz pod adresem `/categories`. Wypisze on listę kategorii posortowanych alfabrtycznie. Każda kategoria powinna być linkiem (na razie pustym), który w przyszłości będzie prowadził do strony produktu.

### Zadanie 3.

Napisz widok, który udostępnisz pod adresem `/category/{slug}` gdzie {slug} to identyfikator tekstowy kategorii. Widok pobierze dane o produktach z tej kategorii i wyświetli produkty w kolejności alfabetycznej. Dane, które mmają być widoczne na ekranie: nazwa, cena.

### Zadanie 4.

Napisz widok, który udostępnisz pod adresem `/product/{id}`, gdzie {id} to identyfikator (klucz główny) produktu. Widok ma wyświetlać metryczkę (wszystkie dane) produktu.

## Dzień 2.

### Zadanie 5.

* Napisz formularz dodawania kategorii produktów do bazy danych:
    * lista kategorii: zmodyfikuj widok `/categories`: przy opisie każdej kategorii, dodaj link **modyfikuj**, na dole listy kategorii dodaj link **dodaj kategorię**, link powinien przekierowywać do adresu `/add_category`
    * edycja kategorii: po wejściu na link do edycji wyświetla się fomrularz edycji kategorii. Można zmienić dane i je zapisać. Formularz edycji kategorii powinien być udostępniony pod adresem `/edit_category/{slug}`. Po zmianie danych powinniśmy zostać przekierowani pod adres `/categories`.
    * dodawanie nowej kategorii: po wejściu na link **dodaj kategorię**, powinien wyświetlić się pusty formularz, w którym można dodać nową kategorię i ją zapisać. Po dodaniu nowej kategorii powinniśmy zostać przekierowani pod adres `/categories`.

### Zadanie 6.

* Napisz formularz dodawania towarów do bazy danych. Dodaj widoki: 
    * lista produktów (udostępniony pod adresem `/products`): wyświetla listę **wszystkich** produktów, niezależnie od kategorii (możesz w tym celu zmodyfikować widok `/category`. Przy opisie każdego progduktu powinien być link do edycji. Parametr powinien być przekazywany w URL-u. Na dole listy osób powinien być link **dodaj produkt**.
    * edycja produktu: po wejściu na link do edycji wyświetla się formularz edycji produktu. Można zmienić dane i je zapisać. Po zmianie danych powinniśmy zostać przekierowani pod adres `/products`.
    * dodawanie produktu: po wejściu w link **dodaj produkt**, powinien wyświetlić się pusty formularz, w którym można dodać nowy towar i go zapisać. Po dodaniu nowego produktu powinniśmy zostać przekierowani pod adres `/products`.

Zadania 1 i 2 z dnia 2, spróbuj rozwiązać używając ModelForms i/lub widoków generycznych.


### Zadanie 7 (*).

* Dodaj formularz wyszukiwania. Powinien mieć tylko jedno pole: szukaj.
* Jeśli formularz został wypełniony poprawnie, powinien wyszukać wpisaną frazę w nazwach produktów **oraz** kategorii i zwrócić znalezione wyniki. 
* Utwórz widok, który zaprezentuje wyniki wyszukiwania. 
* Wartość atrybutu `/name` dla pola szukaj powinna wynosić `search`.
* Widok powinien być udostępniony pod adresem `/search`.

## Dzień 3.

### Zadanie 8.

* Dodaj widok logowania, wraz z odpowiednim formularzem (możesz użyć kodu z zajęć). Widok powinien być udostępniony pod adresem `/login`. Po udanym zalogowaniu powinniśmy zostać przeniesieni na stronę `/products`.

### Zadanie 9.

* Zabezpiecz aplikację w taki sposób, by widoki edycji towaru i kategorii były dostępne tylko dla użytkowników, kótrzy mają przyznane prawa do odpowiednich akcji: "add\_product", "add\_category", "edit\_product", itp. do odpowiednich modeli.

### Zadanie 10.

* Zabezpiecz szablony tak, by linki do odpowiednich akcji (dodaj produkt, modyfikuj produkt, itp.) pojawiały się tylko użytkownikom mającym odpowiednie uprawnienia.

## Dzień 4.

### Zadanie 11.

* Wygeneruj odpowiednie klasy admina dla modeli użytych w pracy domowej. Zapewnij czytelność przez odpowiednie nadpisanie metody `__str__()` (powinny pojawiać się tylko nazwy produktów i kategorii). Zapewnij łatwość użytkowania dodając odpowiednie pola do listy modeli.
