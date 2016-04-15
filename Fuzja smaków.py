#Program stworzy fuzję ulubionych smaków użytkownika
#Adam Orzechowski 8/01

name= input("Jak się nazywasz?")

print("\nWitaj", name, "oto program 'Fuzja Smaków'.")

food1 = input("\nJakie jest Twoje ulubione jedzenie? Zastanów się dobrze :).")

print("\nWięc Twoje ulubione jedzenie to", food1.lower(),
      ",teraz pomyśl o czymś równie smacznym.")

food2 = input("\nCo to za danie?")

input("\nTeraz czas na FUZJĘ, aby rozpocząć naciśnij 'Enter'")

print("\n\n\n\t\t\t", name, ",Twoim wymarzonym jedzeniem jest... \n\n\t\t\t\t\t", food1.upper()+food2.upper(),
      "!!!")

input("\n\n\n\nAby zakończyć naciśnij klawisz Enter.")
