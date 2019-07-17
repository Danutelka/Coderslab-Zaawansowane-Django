<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Formularze &ndash; zadania

#### Pamiętaj, aby wszystkie formularze definiować w pliku **forms.py**!

### Zadanie 1 &ndash; rozwiązywane z wykładowcą.

* Napisz formularz wyszukiwania ucznia. Formularz powinien wyświetlać jedno pole: nazwisko.
* Napisz widok, który:
    * odbierze dane, 
    * wyszuka dane w bazie używając modelu (wystarczy wprowadzić fragment nazwiska, program powinien wyszukać wszysktich uczniów, których nazwiska pasują do wzorca), po czym przekaże je do szablonu i wyświetli wyniki na stronie,
    * widok udostępnij pod URL-em `/student_search`.


---

### Zadanie 2.

* Napisz formularz, który przyjmuje 3 parametry: imię, nazwisko i klasę, do której uczęszcza uczeń. Pole z klasą ucznia powinno przyjmować wartości, które znajdują się w stałej `SCHOOL_CLASS`.
* Napisz widok, który udostępnisz pod adresem `/add_student` 
    * po wejściu metodą GET wyświetli pusty formularz,
    * po wejściu metodą POST odbierze dane z formularza doda ucznia do bazy, po czym przekieruje użytkownika na stronę metryczki danego ucznia.

### Zadanie 3.

Zmodyfikuj widok, model i/lub formularz z poprzedniego zadania. Do modelu dodaj pole `year_of_birth`, które będzie przechowywało wartość typu integer. Pozwól użytkownikowi dodać tę wartość przy pomocy formularza.

### Zadanie 4.

* Napisz formularz, który konwersji walut. Formularz powinien mieć następujące pola:
    * `currency1`: pole przyjmujące liczbę zmiennoprzecinkową,
    * `currency2`: pole przyjmujące liczbę zmiennoprzecinkową,
    * `conversion`: dropdown przyjmujący jedną z dwóch wartości: **PLNtoUSD** i **USDtoPLN**.
* Napisz widok, który udostępnisz pod adresem `/exchange`, który:
    * po wejściu metodą GET wyświetli pusty formularz,
    * po wejściu metodą POST przeliczy waluty ze złotówek na dolary (lub odwrotnie, zależy to od wartości pola `conversion`) i wyświetli wynik.

### Zadanie 5.

* Napisz formularz, który pozwoli dodać oceny uczniowi. Formularz powinien zawierać następujace pola:
    * student: pole z nazwiskiem ucznia,
    * subject: pole z nazwą przedmiotu,
    * grade: pole ze stopniem. Pole powinno przybierać tylko wartości znajdujące się w stałej `GRADES`. 

* Napisz widok, który udostępnisz pod adresem `/add_grade`. Widok powinien definiować następujace funkcjonalności:
    * po wejściu metodą GET, powinen wyświetlić pusty formularz,
    * po wejściu metodą POST, powienien:
        * odebrać dane z formularza,
        * sprawdzić czy dany uczeń istnieje w bazie danych, jeśli nie &ndash; wyświetlić komunikat "Nie ma takiego ucznia!",
        * jeśli dane są poprawne, dopisać uczniowi stopień z danego przemiotu i zapisać do bazy,
        * przekierować użytkownika do strony z danymi ucznia. 
