quiz = [
    {
        "question": "Vilket band räknas ofta som heavy metals grundare?",
        "options": ["A. Metallica", "B. Black Sabbath", "C. Iron Maiden", "D. Slayer"],
        "answer": "B"
    },
    {
        "question": "Vilket land kommer bandet Metallica ifrån?",
        "options": ["A. USA", "B. England", "C. Sverige", "D. Tyskland"],
        "answer": "A"
    },
    {
        "question": "Vilken genre spelar Iron Maiden?",
        "options": ["A. Death metal", "B. Black metal", "C. Heavy metal", "D. Nu metal"],
        "answer": "C"
    },
    {
        "question": "Vad heter Metallicas album 'Master of ___'?",
        "options": ["A. Chaos", "B. Puppets", "C. Fire", "D. Metal"],
        "answer": "B"
    },
    {
        "question": "Vilket band har maskoten Eddie?",
        "options": ["A. Judas Priest", "B. Slayer", "C. Iron Maiden", "D. Megadeth"],
        "answer": "C"
    },

    {
        "question": "Vilken genre är känd för growl-sång?",
        "options": ["A. Power metal", "B. Death metal", "C. Heavy metal", "D. Folk metal"],
        "answer": "B"
    },
    {
        "question": "Vilket land är starkt kopplat till black metal?",
        "options": ["A. USA", "B. Norge", "C. Spanien", "D. Japan"],
        "answer": "B"
    },
    {
        "question": "Vilken genre handlar ofta om vikingar och nordisk mytologi?",
        "options": ["A. Nu metal", "B. Thrash metal", "C. Viking metal", "D. Doom metal"],
        "answer": "C"
    },
    {
        "question": "Vilket svenskt band spelar power metal om krig?",
        "options": ["A. Opeth", "B. Sabaton", "C. Bathory", "D. In Flames"],
        "answer": "B"
    },
    {
        "question": "Vilken genre är oftast snabb och aggressiv?",
        "options": ["A. Doom metal", "B. Thrash metal", "C. Folk metal", "D. Gothic metal"],
        "answer": "B"
    },

    {
        "question": "Vilket instrument är vanligast i metal?",
        "options": ["A. Fiol", "B. Synth", "C. Elgitarr", "D. Saxofon"],
        "answer": "C"
    },
    {
        "question": "Vad kallas metalfans ofta?",
        "options": ["A. Rockers", "B. Metalheads", "C. Goths", "D. Punks"],
        "answer": "B"
    },
    {
        "question": "Vilken genre är långsam och tung?",
        "options": ["A. Doom metal", "B. Thrash metal", "C. Power metal", "D. Speed metal"],
        "answer": "A"
    },
    {
        "question": "Vilket band gjorde albumet 'Paranoid'?",
        "options": ["A. Metallica", "B. Black Sabbath", "C. Megadeth", "D. Slayer"],
        "answer": "B"
    },
    {
        "question": "Vilken genre blandar metal och folkmusik?",
        "options": ["A. Death metal", "B. Folk metal", "C. Black metal", "D. Nu metal"],
        "answer": "B"
    },

    {
        "question": "Vilken genre blev populär runt år 2000?",
        "options": ["A. Heavy metal", "B. Doom metal", "C. Nu metal", "D. Thrash metal"],
        "answer": "C"
    },
    {
        "question": "Vilket band gjorde albumet 'Hybrid Theory'?",
        "options": ["A. Slipknot", "B. Korn", "C. Linkin Park", "D. Disturbed"],
        "answer": "C"
    },
    {
        "question": "Vilken genre använder ofta corpse paint?",
        "options": ["A. Power metal", "B. Black metal", "C. Folk metal", "D. Nu metal"],
        "answer": "B"
    },
    {
        "question": "Vilken genre har ofta fantasiteman?",
        "options": ["A. Power metal", "B. Death metal", "C. Doom metal", "D. Thrash metal"],
        "answer": "A"
    },
    {
        "question": "Vilket band är känt för låten 'Chop Suey!'?",
        "options": ["A. Korn", "B. Slipknot", "C. System of a Down", "D. Limp Bizkit"],
        "answer": "C"
    },

    {
        "question": "Vilket land kommer bandet Sabaton ifrån?",
        "options": ["A. Norge", "B. Finland", "C. Sverige", "D. Tyskland"],
        "answer": "C"
    },
    {
        "question": "Vilken genre kombinerar punk och metal?",
        "options": ["A. Metalcore", "B. Doom metal", "C. Folk metal", "D. Prog metal"],
        "answer": "A"
    },
    {
        "question": "Vilken genre har ofta väldigt långa låtar?",
        "options": ["A. Nu metal", "B. Progressive metal", "C. Thrash metal", "D. Speed metal"],
        "answer": "B"
    },
    {
        "question": "Vilken genre är känd för blast beats?",
        "options": ["A. Death metal", "B. Doom metal", "C. Power metal", "D. Folk metal"],
        "answer": "A"
    },
    {
        "question": "Vilket band gjorde albumet 'Reign in Blood'?",
        "options": ["A. Metallica", "B. Slayer", "C. Megadeth", "D. Anthrax"],
        "answer": "B"
    }
]
import random

playing = True

while playing:
    score = 0
    random.shuffle(quiz)  

    for q in quiz:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        answer = ""
        while answer not in ["A", "B", "C", "D"]:
            answer = input("Ditt svar (A/B/C/D): ").upper()
            if answer not in ["A", "B", "C", "D"]:
                print("Fel input, välj A, B, C eller D.")

        if answer == q["answer"]:
            print("Rätt!")
            score += 1
        else:
            print(f"Fel! Rätt svar var {q['answer']}")

    print(f"\nResultat: {score} av {len(quiz)} rätt")

    again = input("Vill du spela igen? (j/n): ").lower()
    if again != "j":
        playing = False

print("Tack för att du spelade ")
