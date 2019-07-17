# Użytkownicy &ndash; zadania

### Zadanie 1 &ndash; rozwiązywane z wykładowcą.

* Używając `./manage.py` dodaj superużytkownika.
* Napisz widok, który udostępnisz pod adresem `/list_users`. Po wejściu metodą GET:
    * pobierz dane wszystkich użytkowników z bazy,
    * wyświetl ich loginy i nazwiska na stronie.

---

### Zadanie 2.
* Napisz widok `/login`, który:
    * po wejściu metodą GET, wyświetli formularz logowania (użytkownik i hasło)
    * po wejściu metodą POST, przeprwadzi autentykację i logowanie.
        * w razie błędów, poinformuje o tym użytkownika. 

* Napisz widok `/logout`, który wyloguje użytkownika. 

* Utwórz widok bazowy, który:
    * w stopce będzie pokazywał aktualnie zalogowanego użytkownika.
    * w zależności od tego, czy jakiś użytkownik jest zalogowany, czy nie pokaże link do widoku `/login` lub `/logout`.


### Zadanie 3.
* Napisz widok `/add_user`, który:
    * po wejściu metodą GET, wyświetli formularz dodawania użytkownika do wypełnienia:
        * login,
        * hasło (pamiętaj o odpowiednim widgecie),
        * ponowne hasło,
        * imię,
        * nazwisko,
        * email,
    * po wejściu metodą POST, sprawdzi poprawność formularza:
        * czy login jest już zajęty,
        * czy hasło i ponowne hasło są takie same,
        * czy email jest poprawny,
    * jeśli dane są poprawne, założy użytkownika,
    * jeśli błędne &ndash; poinformuje użytkownika o błędzie.

### Zadanie 4.
* Napisz widok `/reset_password/{id}`, gdzie id to identyfikator użytkownika, który:
    * po wejściu metodą GET, wyświetli formularz zmiany hasła użytkownika do wypełnienia:
        * wprowadź nowe hasło,
        * ponownie wprowadź nowe hasło,
    * po wejściu metodą POST, sprawdzi poprawność formularza:
        * czy nowe hasło i ponowne hasło są takie same,

    * jeśli dane są poprawne, zmieni hasło użytkownika,
    * jeśli błędne &ndash; poinformuje użytkownika o błędzie.

Pamiętaj o odpowiednich widgetach.


