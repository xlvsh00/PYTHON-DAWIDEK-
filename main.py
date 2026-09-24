def menu():
    print("-SYSTEM ZARZĄDZANIA ZADANIAMI-")
    print("1. Dodaj nowe zadanie")
    print("2. Wyświetl wszystkie zadania")
    print("3. Wyszukaj zadanie")
    print("4. Oznacz zadanie jako wykonane")
    print("5. Usuń zadanie")
    print("6. Wyjdź z programu")

def dodaj_zadanie(zadania):
    print("Dodawanie nowego zadania")
    
    nazwa = input("Podaj nazwę zadania: ")
    osoba = input("Podaj przypisaną osobę (imię i nazwisko): ")
    priorytet = input("Podaj priorytet (wysoki, średni, niski): ")
    status = "w trakcie"
    kategorie_input = input("Podaj kategorie oddzielone przecinkami (np. backend, baza danych): ")
    
