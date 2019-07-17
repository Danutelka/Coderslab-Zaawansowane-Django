<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# ModelForms i widoki generyczne &ndash; zadania

### Zadanie 1 &ndash; rozwiązywane z wykładowcą.

* Napisz formularz dziedziczący po klasie ModelForm, który pozwala na dodanie przedmiotu do bazy danych.
* Napisz widok, który:
    * Po wejściu metodą GET, wyświetli pusty formularz,
    * Po wejściu metodą POST, zapisze model powiązany z formularzem do bazy danych.

---

### Zadanie 2.

* Napisz model `Message`, który będzie reprezentował maila do nauczyciela danego przedmiotu. Model powinien mieć następujące pola:
    * `subject`: pole tekstowe, max. 256 znaków,
    * `content`: pole tekstowe o nieograniczonej liczbie znaków,
    * `to`: klucz obcy do przedmiotu (nauczyciela),
    * `from`: klucz obcy do ucznia,
    * `date_sent`: pole typu datetime, automatycznie uzupełniane przy zapisie.

* Napisz formularz dziedziczący po klasie ModelForm, który będzie pozwalał na obsługę modelu `Message`. Formularz ma udostępniać wszystkie pola oprócz `date_sent`.

* Napisz widok (udostępnij pod URL-em `/compose_message`), który:
    * po wejściu metodą GET, wyświetli formularz,
    * po wejściu metodą POST, zapisze maila do bazy.


### Zadanie 3.

* Napisz model `StudentNotice`, który będzie reprezentował uwagi od nauczycieli dla uczniów. Model powinien mieć następujące pola:
    `from`: klucz obcy do przemiotu (nauczyciela),
    `to`: klucz obcy do ucznia,
    `content`: pole tekstowe o nieograniczonej liczbie znaków.

* Napisz formularz dziedziczący po klasie ModelForm, który będzie pozwalał na obsługę modelu `StudentNotice`.

* Napisz widok, który udostępnisz pod adresem `/notices/{student_id}`, gdzie id to identyfikator ucznia. Widok powinien wyciągnąć z bazy wszystkie uwagi dla danego ucznia i zaprezentować je na stronie. W szablonie umieść też odpowiednie linki dla nauczyciela do dodawania i usuwania istniejących uwag.

### Zadanie 4.

* Napisz widoki, dziedziczące po widokach generycznych, które umożliwią dodanie i usunięcie uwagi dla ucznia.
