import time

def slowprint(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.01)
    print()

def skapa_profil():
    print("\n--- Skapa din träningsprofil ---")
    namn = input("Vad heter du? ")
    ålder = input("Hur gammal är du? ")
    erfarenhet = input("Hur länge har du tränat? (t.ex 1 år, nybörjare, 5+ år): ")
    mål = input("Vad är ditt övergripande träningsmål? ")

    profil = {
        "namn": namn,
        "ålder": ålder,
        "erfarenhet": erfarenhet,
        "mål": mål
    }

    print("\nDin profil har sparats! ✔")
    return profil

def visa_program(mål):
    print("\n--- Ditt rekommenderade program ---")

    if mål == 1:
        print(" Bodybuilding-program (Hypertrofi):")
        print("""
Push–Pull–Legs upplägg:
• Reps: 8–12
• Set: 3–4 per övning
• Fokus: Muskelkontakt, pump, progressiv överbelastning
""")

    elif mål == 2:
        print(" Powerlifting-program (Styrka):")
        print("""
3-dagars styrkefokus:
• Måndag: Marklyft + assisterande rygg
• Onsdag: Bänkpress + triceps
• Fredag: Knäböj + ben
• Reps: 3–5
• Set: 4–6
""")

    elif mål == 3:
        print(" Viktnedgångsprogram:")
        print("""
Kombinerad styrka + cardio:
• 3 styrkepass/vecka
• 2 intervallpass
• Kost: Lätt kaloriunderskott
""")

    elif mål == 4:
        print(" Anpassat mål:")
        print("Stefan kontaktar dig baserat på din profil och dina svar!")

def huvudmeny():
    slowprint("Hej och välkommen till Stefans online coaching!")
    
    profil = None

    while True:
        print("\n--- Huvudmeny ---")
        print("1. Skapa/ändra träningsprofil")
        print("2. Välj coachingmål")
        print("3. Se rekommenderat träningsprogram")
        print("4. Avsluta programmet")

        val = input("Välj ett alternativ (1–4): ")

        if val == "1":
            profil = skapa_profil()

        elif val == "2":
            print("\n--- Välj ditt mål ---")
            print("1. Bodybuilding")
            print("2. Powerlifting")
            print("3. Viktnedgång")
            print("4. Anpassat mål")

            mål_val = input("Skriv siffran för ditt val: ")

            if mål_val.isdigit() and 1 <= int(mål_val) <= 4:
                global valt_mål
                valt_mål = int(mål_val)
                print("Mål uppdaterat! ")
            else:
                print("Ogiltigt val!")

        elif val == "3":
            if 'valt_mål' not in globals():
                print("\nDu måste välja ett mål först!")
            else:
                visa_program(valt_mål)

        elif val == "4":
            print("Tack för att du testade Stefano Coaching! ")
            break

        else:
            print("Fel input! Försök igen.")

# Startar programmet
huvudmeny()