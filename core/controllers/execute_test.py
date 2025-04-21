from typing import Optional

from peewee import DoesNotExist
from telegram import User as TelegramUser

from core.controllers.permission import PermissionController
from core.controllers.result_test import ResultTestController, TestResult
from db.permissions import User
from db.quiz import Answer, PassingAnswer, PassingTest, Question, Test


class ExecuteTestController:
    class TestNotFound(Exception):
        def __init__(self):
            super().__init__("Тест не существует")

    def __init__(self, user: User, test: Test):
        self.user = user
        self.test = test
        self.questions = list(test.questions)
        self.passing = PassingTest.create(
            test=self.test,
            respondent=self.user
        )

    @property
    def test_name(self):
        return self.test.name

    @staticmethod
    def create(telegram_user: TelegramUser, test_id: int) -> 'ExecuteTestController':
        try:
            user = PermissionController.get_user_by_telegram(telegram_user).user
            test = Test.get(id=test_id)
            return ExecuteTestController(user, test)
        except DoesNotExist:
            raise ExecuteTestController.TestNotFound()

    def get_question(self) -> Optional[Question]:
        if self.questions:
            return self.questions[0]
        return None

    def get_answers(self) -> [Answer]:
        question = self.get_question()
        if question:
            return Answer.filter(question=question)
        return []

    def _next_question(self):
        self.questions.pop(0)

    def answer(self, answer_id: int):
        answer = Answer.get(id=answer_id)
        PassingAnswer.create(
            passing=self.passing,
            question=answer.question,
            current_answer=answer
        )
        self._next_question()

    def get_result_statistic(self) -> TestResult:
        return ResultTestController(self.passing).get_result()
