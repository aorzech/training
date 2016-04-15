#Ten program obliczy ile trzeba zapłacić napiwku kelnerowi
#Adam Orzechowski 8/01/2015

bill = float(input("Ile zapłaciłeś ostatnio w restauracji? Kwotę podaj w złotych. Zapłaciłem:"))

print("\nOk, więc zapłaciłeś:", bill, "zł.")

print("\n\nJeśli chcesz zapłacić napiwek wysokości 15%, bez groszy, będzie wynosił", bill * 0.15//1, "zł.")
print("\nJeśli chcesz zapłacić napiwek wysokości 20%, (również bez zbędnej końcówki) będzie on wynosił około", bill * 0.2//1, "zł.")
                
input("\n\nAby zakończyć naciśnij 'Enter'")
