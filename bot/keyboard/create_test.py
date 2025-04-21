from telegram import InlineKeyboardButton, InlineKeyboardMarkup

START = 'start'
ADD = 'add'
SKIP = 'skip'
END = 'END'

def get_start_create_test_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Начать", callback_data=START),
        ]
    ])

def get_create_test_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("Добавить", callback_data=ADD),
            InlineKeyboardButton("Следующий", callback_data=SKIP),
        ],
        [
            InlineKeyboardButton("Закончить", callback_data=END),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
