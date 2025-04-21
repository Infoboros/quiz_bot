from peewee import DoesNotExist

from core.controllers.result_test import ResultTestController, TestResult
from db.permissions import User
from db.quiz import Test


class StatisticsController:
    class TestNotFound(Exception):
        def __init__(self, test_id):
            super().__init__(f"Тест с идентификаторов {test_id} не найден")

    def __init__(self, user: User):
        self.user = user

    def get_tests(self) -> [Test]:
        return Test.filter(owner=self.user)

    def get_test_statistic(self, test_id: int) -> [TestResult]:
        try:
            test = Test.get(id=test_id, owner=self.user)
            return [
                ResultTestController(passing).get_result()
                for passing in test.passing
            ]
        except DoesNotExist:
            raise self.TestNotFound(test_id)
