from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass
class UserStore:
    """Enkel användardatabas i minnet."""
    users: Dict[str, str]

    def verify(self, username: str, password: str) -> bool:
        return username in self.users and self.users[username] == password


DEFAULT_STORE = UserStore(users={"test": "1234"})


def login_user(username: str, password: str, store: UserStore = DEFAULT_STORE) -> bool:
    """Testbar login-funktion (ingen input/print)."""
    return store.verify(username.strip(), password)
