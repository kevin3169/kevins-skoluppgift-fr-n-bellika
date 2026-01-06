from quiz.quiz_data import QUIZ
from quiz.quiz_logic import load_questions, check_answer, is_valid_answer, score_quiz


def test_quiz_data_is_valid():
    questions = load_questions(QUIZ)
    assert len(questions) >= 5
    for q in questions:
        assert isinstance(q.question, str) and q.question
        assert len(q.options) == 4
        assert q.answer in {"A", "B", "C", "D"}


def test_check_answer_case_and_spaces():
    assert check_answer(" a ", "A") is True
    assert check_answer("b", "A") is False


def test_is_valid_answer():
    assert is_valid_answer("A")
    assert is_valid_answer(" d ")
    assert not is_valid_answer("")
    assert not is_valid_answer("E")


def test_score_quiz_counts_correct():
    questions = load_questions(QUIZ)[:3]
    answers = [questions[0].answer, "Z", questions[2].answer]
    assert score_quiz(questions, answers) == 2
