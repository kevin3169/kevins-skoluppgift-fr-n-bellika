from __future__ import annotations

import random
from typing import List

from quiz.quiz_data import QUIZ
from quiz.quiz_logic import load_questions, is_valid_answer, normalize_answer, score_quiz


def run_cli_quiz() -> None:
    questions = load_questions(QUIZ)
    random.shuffle(questions)

    answers: List[str] = []
    for q in questions:
        print("\n" + q.question)
        for opt in q.options:
            print(opt)

        ans = ""
        while not is_valid_answer(ans):
            ans = input("Ditt svar (A/B/C/D): ")
            if not is_valid_answer(ans):
                print("Fel input, välj A, B, C eller D.")

        answers.append(normalize_answer(ans))

    score = score_quiz(questions, answers)
    print(f"\nResultat: {score} av {len(questions)} rätt")
    print("Tack för att du spelade 🤘")


if __name__ == "__main__":
    run_cli_quiz()
