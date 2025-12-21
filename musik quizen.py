def run_quiz(frågor):
    score = 0
    for f in frågor:
        svar = input(f["frågor"] + "").lower()
        if svar == f["svar"]:
            print("rätt svar")
            score += 1
        else:
            print("print fel svar 0 poäng")

    return score         

    
print ("Hej och välkommen till Musik quizen om METAL")


