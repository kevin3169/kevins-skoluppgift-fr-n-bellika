from quiz.login import UserStore, login_user


def test_login_success():
    store = UserStore(users={"neslihan": "hemligt"})
    assert login_user("neslihan", "hemligt", store=store) is True


def test_login_fail_wrong_password():
    store = UserStore(users={"neslihan": "hemligt"})
    assert login_user("neslihan", "fel", store=store) is False


def test_login_strips_username():
    store = UserStore(users={"user": "pw"})
    assert login_user("  user  ", "pw", store=store) is True
