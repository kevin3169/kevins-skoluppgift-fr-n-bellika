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
