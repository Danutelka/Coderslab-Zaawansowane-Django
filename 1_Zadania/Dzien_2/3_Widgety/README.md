<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Widgety &ndash; zadania

#### Zadanie 1 &ndash; wykonywane razem z wykładowcą.

* Napisz formularz, który będzie pozwalał skomponować dodatki do pizzy. 
* Powinien mieć tylko jedno pole, za to wielokrotnego wyboru. Wartości, które będzie można wybrać, to:
    * oliwki,
    * pomidory,
    * dodatkowy ser,
    * anchovies,
    * cebula.
* Napisz widok, po wejściu na niego metodą GET, wyświetl formularz. 
* Zmień widget pola na `CheckboxSelectMutiple` i porównaj różnice.

W katalogu 4_Snippety znajdują się gotowe modele do tego zadania.

---

### Zadanie 2.

* Napisz model `PresenceList`, który będzie przechowywał listę obecności ucznia na lekcjach. Model powinien mieć następujące pola:
    * student: klucz obcy do modelu `Student`,
    * day: pole typu date (tylko data) &ndash; dzień lekcyjny,
    * present: wartość logiczna, powinna pozwalać na brak wartości (null).

* Napisz formularz, który będzie zawierał dane, jak w powyższym modelu,

* Napisz widok, który udostępnisz pod adresem `/class_presence/{student_id}/{date}`, gdzie {student_id} to identyfikator ucznia, a {date} to dzień w szkole. 
    * po wejściu metodą GET, widok powinien wyświetlić formularz dla daty podanej w parametrze. Pole `day` powinno być ukryte (użyj widgetu `HiddenInput`),
    * po wejściu metodą POST, widok powinen zapisać dane o obecności ucznia.
    

### Zadanie 3. 

* Napisz formularz z jednym polem: `background_color`. Pole to powinno pozwalać na wpisanie 5 wartości: black, white, red, yellow i blue,

* Napisz widok, który udostępnisz pod adresem `/set_color`. 
    * po wejściu metodą GET, widok  powinien pokazać formularz. Pole `background_color` powinno używać widgetu `RadioSelect`,
    * po wejściu metodą POST, widok powininen pokazać formularz j.w. Dodatkowo powinno zmienić się tło na kolor wybrany przez użytkownika.

### Zadanie 4.

* Napisz formularz logowania z dwoma polami: `login` i `password`. Pole `password` powinno używać widgetu `PasswordInput`, 
* Napisz widok, który udostępnisz pod adresem `/login`. Widok po wejściu metodą GET, ma wyswietlić pusty formularz logowania.
* Napisz metodę `post()` do poprzedniego zadania, która odbierze dane z formularza, sprawdzi, czy użytkownik to **root**, a hasło, to **very\_secret**. Jeśli tak, pokaże na ekranie przeglądarki "Miło Cię widzieć", jeśli nie &ndash; "A sio, hackerze!".
