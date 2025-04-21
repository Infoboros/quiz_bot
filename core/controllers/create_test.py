from typing import Optional

from db.permissions import User
from db.quiz import Question, Test


class CreateTest:
    def __init__(self, user: User, name: str):
        self.user = user
        self.test = Test.create(owner=user, name=name)
        self.questions = self._get_user_questions()
        self.questions_for_test = []

    def _get_user_questions(self) -> [Question]:
        return list(
            Question
            .select()
            .where(
                (Question.owner == self.user)  # сравнение с конкретным значением
                | Question.owner.is_null()  # или проверка на NULL
            )
        )

    def _pop(self):
        return self.questions.pop(0)

    def get_next(self) -> Optional[Question]:
        return self.questions[0] if self.questions else None

    def add(self):
        self.test.questions.add(self._pop())

    def skip(self):
        self._pop()
