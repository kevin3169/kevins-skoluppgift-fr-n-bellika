from __future__ import annotations

import random
import tkinter as tk
from tkinter import messagebox

from quiz.quiz_data import QUIZ
from quiz.quiz_logic import load_questions, check_answer


def start_gui_quiz() -> None:
    questions = load_questions(QUIZ)
    random.shuffle(questions)

    current = 0
    score = 0

    root = tk.Tk()
    root.title("Metal Quiz")
    root.geometry("650x380")

    question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=600)
    question_label.pack(pady=20)

    def show_question() -> None:
        q = questions[current]
        question_label.config(text=q.question)
        for i in range(4):
            buttons[i].config(text=q.options[i])

    def on_answer(letter: str) -> None:
        nonlocal current, score
        correct = questions[current].answer

        if check_answer(letter, correct):
            score += 1
            messagebox.showinfo("Rätt", "Rätt svar! 🤘")
        else:
            messagebox.showerror("Fel", f"Fel svar 😢\nRätt svar var {correct}")

        current += 1
        if current < len(questions):
            show_question()
        else:
            messagebox.showinfo("Resultat", f"Du fick {score} av {len(questions)} rätt!")
            root.destroy()

    buttons = []
    for letter in ["A", "B", "C", "D"]:
        btn = tk.Button(
            root,
            text="",
            font=("Arial", 14),
            width=35,
            command=lambda l=letter: on_answer(l),
        )
        btn.pack(pady=5)
        buttons.append(btn)

    show_question()
    root.mainloop()


if __name__ == "__main__":
    start_gui_quiz()
