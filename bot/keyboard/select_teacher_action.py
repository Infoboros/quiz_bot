from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from bot.handlers.teacher.states import LIST_TEST, LOAD_QUESTIONS, SHOW_TEST_RESULT, START_CREATE_TEST


def get_select_teacher_action_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("Загрузить вопросы", callback_data=LOAD_QUESTIONS),
        ],
        [
            InlineKeyboardButton("Создать тест", callback_data=START_CREATE_TEST),
            InlineKeyboardButton("Список тестов", callback_data=LIST_TEST),
        ],
        [InlineKeyboardButton("Посмотреть результаты", callback_data=SHOW_TEST_RESULT), ],
        [
            InlineKeyboardButton("Назад", callback_data="cancel"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
