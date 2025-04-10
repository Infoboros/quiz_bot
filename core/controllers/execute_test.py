from typing import Optional

from peewee import DoesNotExist

from db.quiz import Question, Test


class ExecuteTestController:

    class TestNotFound(Exception):
        def __init__(self):
            super().__init__("Тест не существует")

    def __init__(self, test: Test):
        self.test = test
        self.questions = list(test.questions)

    def get_question(self) -> Optional[Question]:
        if self.questions:
            return self.questions.pop(0)
        return None

    @property
    def test_name(self):
        return self.test.name

    @staticmethod
    def create(test_id: int):
        try:
            test = Test.get(id=test_id)
            return ExecuteTestController(test)
        except DoesNotExist:
            raise ExecuteTestController.TestNotFound()