lista = ["Aries","Taurus","Gemini","Cancer","Leo"]

meny = 0
delet = 0

print("Välkommen till programmet. \n")

while meny != 4:
    meny = int(input(" 1. Visa listan. \n 2. Skriv lägg till på listan. \n 3. Rensa listan. \n 4. Avsluta programmet. \n"))
    print("\n")
    if meny == 1:
        for l in lista:
            print(l)
    if meny == 2:
        addition = input("Skriv till på listan: ")
        lista.append(addition)
    if meny == 3:
        delet = int(input("Är du säker? Skriv 1 och ENTER för att bekräfta: "))
        if delet == 1:
            lista.clear
            print("Lista rensad.")
        else:
            print("Rensning avbruten.")
            delet = 0
    print("\n")