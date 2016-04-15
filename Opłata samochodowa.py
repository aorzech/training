#Program podatekod samochodu
#Adam Ozechowski 10/01

price = int(input("Oto program cena samochodu, zobaczysz ile musisz dodadkowo zapłacić \n, za swoje nowe cacko. Ile złotych kosztuje auto?"))

print("\n\n\t\t\t\tOPŁATY:")

fee1=125
fee2=price*0.12
fee3=fee2*2.5
fee4=25


print("\nOpłata za rejestracje", fee1, "zł.")

print("\nOpłata środowiskowa", fee2, "zł.")

print("\nŁapówka dla GDOŚ", fee3, "zł.")

print("\nŁapówka dla policji", fee4, "zł.")

print("\nŁączny koszt wynosi", fee1+fee2+fee3+fee4+price, "zł")

input("\n\n\nABy zakończyć wciśniej 'Enter'")
