import io
from collections import Counter
from itertools import count

from packaging import tags

from db.permissions import User
from db.quiz import Answer, Question, Tag


class ImportQuestionController:

    def __init__(
            self,
            user: User,
            file: io.BytesIO
    ):
        self.file = file
        self.user = user

    def import_question(self, unicode_line: str) -> Question:
        print(unicode_line)
        print(11111)
        tag, question, *answers = unicode_line.split(";")
        tag, _ = Tag.get_or_create(name=tag)

        question, _ = Question.get_or_create(
            owner=self.user,
            question=question
        )
        question.tags.clear()
        question.tags.add(tag)
        Answer.delete().where(Answer.question == question).execute()

        answers_with_count = Counter(answers)
        for answer, count in answers_with_count.items():
            Answer.create(
                question=question,
                answer=answer,
                is_correct=count > 1
            )

    def import_questions(self) -> [Question]:
        return [
            self.import_question(line.decode('utf-8').strip().replace(".", ""))
            for line in self.file.readlines()
        ]
