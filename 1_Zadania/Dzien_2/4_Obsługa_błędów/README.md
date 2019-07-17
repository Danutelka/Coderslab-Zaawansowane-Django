<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Obsługa błędów &ndash; zadania

#### Zadanie 1 &ndash; wykonywane razem z wykładowcą.
* Napisz formularz, który przyjmie od użytkownika następujące pola:
    * imię,
    * nazwisko,
    * email,
    * ulubiona strona www.
* Pola email i www, niech będą walidowane odpowiendimi walidatorami (sprawdź w dokumantacji pod adresem https://docs.djangoproject.com/en/1.10/ref/validators/#emailvalidator).
* Napisz widok, który udostępnisz pod adresem `/d2_p3_e1`, który:
    * po wejściu metodą GET wyświetli pusty formularz,
    * po wejściu metodą POST sprawdzi poprawność danych i wypisze ew. błędy. W przypadku poprawnych danych, niech je pokaże w przeglądarce. 

---

#### Zadanie 2.

* Napisz walidator, który sprawdzi czy walidowana liczba jest w zakresie 2000 - 2004. 
* Użyj tego walidatora, aby sprawdzić poprawność danych w formularzu z zadania 3 z działu **1_Formularze**.

#### Zadanie 3.

* Napisz formularz, który pozwoli Ci wprowadzić imię i nazwisko.
* Do formularza dodaj walidator, który sprawdzi, czy imię jest żeńskie. Jeśli nie, poinformuj o błędzie użytkownika. 
* Napisz widok, który udostępnisz pod adresem `/d2_p3_e3`, który:
    * po wejściu metodą GET wyświetli pusty formularz,
    * po wejściu metodą POST sprawdzi poprawność danych i wypisze ew. błędy. W przypadku poprawnych danych, niech je pokaże w przeglądarce. 
 
##### Hint: Przyjmij, że żeńskie imiona to te, które kończą się literą "a". Wyjątki (np. Barnaba, Kuba) możesz zignorować.

#### Zadanie 4.
* Napisz formularz, który pozwoli Ci wprowadzić liczbę i string,
* Do formularza dodaj walidator, który sprawdzi, czy liczba jest z zakresu 1 - 100.
* Napisz widok, który udostępnisz pod adresem `/d2_p3_e4`, który:
    * po wejściu metodą GET wyświetli pusty formularz,
    * po wejściu metodą POST sprawdzi poprawność danych i wypisze ew. błędy. W przypadku poprawnych danych, wypisze string tyle razy, jaką liczbę wprowadzono.

