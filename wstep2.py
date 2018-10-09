imie = input("Podaj sowoje imię:\n")
nazwisko = input("Podaj sowoje\n imienionazwisko:")

try:
        wiek = int(input("Podaj swój wiek nóbie"))
except ValueError as owcaError :
    wiek = 8
    print( f'wiek ustawiono na {wiek},\n wystapill {owcaError}')


numerkarty = input("Dawaj karte\n na kopary:")
kodCVC = input("Podaj numer CVC:\n To jest skam.")

