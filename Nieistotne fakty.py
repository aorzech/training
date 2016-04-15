#Nieistotne fakty
#
#Uzyskuje osobiste dane użytownika, potem
#Przekształca je w prawdziwe lecz bezużyteczne fakty.
#Adam Orzechowski - kontunuuję swoją przygodę z programowaniem

name = input("Siemka! Jak masz na imię?")

age = input("Ile masz lat?")
age = int(age)

weight = int(input("Jaka jest Twoja waga?"))

print("\nJeśli poeata ee cummings wysłałby do Ciebie wiadomość email, nazwałby CIę",
      name.lower())

print("\nJeśli byłby wściekły napisałby", name.upper())

called = name * 5
print("\nJeśli dziecko miałoby Cię zawołać, zabrzmiało by to pewnie tak:",
                 called)

seconds = age*365*24*60*60
print("\nŻyjesz już ponad:", seconds, "sekund.")

moon_weight=weight/6
print("\nCzy wiesz, że na Księżycu Twoja waga wynosiłaby:", moon_weight, "kg?")

sun_weight=weight*27.1
print("\nCzy wiesz, że na Słońcu Twoja waga wynosiłaby:", sun_weight, "kg (ale niestety niedługo)")

input("\n\nAby zakończyć naciśnij klawisz Enter.")
           
