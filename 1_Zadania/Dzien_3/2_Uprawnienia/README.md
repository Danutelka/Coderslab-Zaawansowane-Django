# Uprawnienia &ndash; zadania

### Zadanie 1 &ndash; rozwiązywane z wykładowcą.
Zmodyfikuj zadanie 4 z poprzedniego rozdziału tak, aby tylko użytkownik posiadający uprawnienie "change_user" mógł wejść do tego widoku.

---

### Zadanie 2.

W aplikacji masz widok `/notices`, który napisałeś kilka dni temu. Zmodyfikuj ten widok (lub template) tak, by:
* tylko użytkownik z uprawnieniem "add\_student\_notice" mógł wysłać uwagę do ucznia,

Następnie dodaj zwykłego użytkownika do aplikacji i nadając / usuwając odpowiednie uprawnienia przetestuj ten widok. wykorzystaj widok do logowania, który napisałeś w  poprzednim rozdziale, aby się zalogować na tego użytkownika.

### Zadanie 3.
* Dodaj ręcznie grupę "teachers", która będzie miała prawa do dodawania notatek i sprawdzania obecności.
* Dodaj ręcznie zwykłego użytkownika, którego dodasz do grupy "teachers",
* Dodaj ręcznie zwykłego użytkownika, który nie będzie nie będzie dodany do ww. grupy i nie będzie miał ww. uprawnień.

Przetestuj uprawnienia użytkowników.
