import io

from openpyxl.reader.excel import load_workbook

from db.permissions import User
from db.quiz import Answer, Question


class ImportQuestionController:

    def __init__(
            self,
            user: User,
            file: io.BytesIO
    ):
        self.wb = load_workbook(file)
        self.user = user

    def import_questions(self) -> [Question]:
        # TODO нормальный импорт
        question, _ = Question.get_or_create(
            owner=self.user,
            question="Ответ на главный вопрос жизни и всего такого"
        )

        Answer.get_or_create(
            question=question,
            answer="42",
            is_correct=True
        )
        Answer.get_or_create(
            question=question,
            answer="24",
            is_correct=False
        )

        return [question]
