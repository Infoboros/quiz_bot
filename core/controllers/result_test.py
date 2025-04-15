import dataclasses

from db.quiz import PassingAnswer, PassingTest, Question


@dataclasses.dataclass
class TestResult:
    test_name: str
    all_questions: int
    answers: int
    correct_answers: int

    @property
    def correct_percentage(self) -> float:
        return self.correct_answers / self.all_questions * 100 if self.all_questions else 0


class ResultTestController:
    def __init__(self, passing_test: PassingTest):
        self.passing_test = passing_test

    def get_result(self) -> TestResult:
        test = self.passing_test.test
        passing_answers = PassingAnswer.filter(passing=self.passing_test)
        return TestResult(
            test_name=test.name,
            all_questions=test.questions.count(),
            answers=passing_answers.count(),
            correct_answers=passing_answers.filter(current_answer__is_correct=True).count(),
        )
