from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Dict, Any


VALID_ANSWERS = {"A", "B", "C", "D"}


@dataclass(frozen=True)
class Question:
    question: str
    options: List[str]  # exakt 4
    answer: str         # "A"|"B"|"C"|"D"


def normalize_answer(s: str) -> str:
    """Trimma och gör versal."""
    return (s or "").strip().upper()


def is_valid_answer(s: str) -> bool:
    return normalize_answer(s) in VALID_ANSWERS


def check_answer(user_answer: str, correct_answer: str) -> bool:
    """Returnerar True om svaret är korrekt."""
    return normalize_answer(user_answer) == normalize_answer(correct_answer)


def load_questions(raw: Iterable[Dict[str, Any]]) -> List[Question]:
    """Validera och konvertera dict-lista till Question-objekt."""
    questions: List[Question] = []
    for idx, q in enumerate(raw):
        if "question" not in q or "options" not in q or "answer" not in q:
            raise ValueError(f"Fråga #{idx} saknar nycklar (question/options/answer).")

        question = str(q["question"])
        options = list(q["options"])
        answer = normalize_answer(str(q["answer"]))

        if len(options) != 4:
            raise ValueError(f"Fråga #{idx} måste ha exakt 4 alternativ.")
        if answer not in VALID_ANSWERS:
            raise ValueError(f"Fråga #{idx} har ogiltigt svar '{answer}'. Måste vara A-D.")

        questions.append(Question(question=question, options=options, answer=answer))
    return questions


def score_quiz(questions: Iterable[Question], answers: Iterable[str]) -> int:
    """Räkna poäng givet frågor + användarens svar (i samma ordning)."""
    score = 0
    for q, a in zip(questions, answers):
        if check_answer(a, q.answer):
            score += 1
    return score
