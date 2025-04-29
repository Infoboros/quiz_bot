from telegram import Update
from telegram.ext import ContextTypes

from bot.handlers.mode.states import TEACHER
from bot.handlers.teacher.states import CREATE_TEST, START_CREATE_TEST
from bot.keyboard.create_test import ADD, END, get_create_test_keyboard, SKIP
from bot.messages.mode import print_message_state_change as print_message_state_change_mode
from bot.messages.teacher import print_message_state_change
from core.controllers.create_test import CreateTest
from core.controllers.permission import PermissionController


async def start_create_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("start_create_test")
    try:
        print("create test create_test_controller")
        context.user_data["create_test_controller"] = CreateTest(
            PermissionController.get_user_by_telegram(
                update.effective_user
            ).user,
            update.message.text
        )
        return await print_message_state_change(START_CREATE_TEST, CREATE_TEST, context, update.message.chat.id)

    except Exception as e:
        await update.message.reply_text(f"Ошибка создания теста {e}")
        return await print_message_state_change(START_CREATE_TEST, START_CREATE_TEST, context, update.message.chat.id)


async def create_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("create_test")
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    action = query.data

    controller: CreateTest = context.user_data.get("create_test_controller")

    if action == ADD:
        print("create test add")
        controller.add()
    if action == SKIP:
        print("create test skip")
        controller.skip()

    question = controller.get_next()
    if question and (action != END):
        print("create test next")
        await query.edit_message_text(
            f"<b>Теги</b>: {', '.join(map(str, question.tags))}\n"
            f"<b>Вопрос</b>: {question.question}",
            reply_markup=get_create_test_keyboard(),
            parse_mode="HTML",
        )
        return CREATE_TEST
    else:
        print("create test end")
        print(controller.questions_for_test)
        test = controller.test
        await query.edit_message_text(
            f"Создан тест: <b>{test.name}</b>\n"
            f"Идентификатор теста: <b>{test.id}</b>\n"
            f"Количество вопросов: <b>{len(test.questions)}</b>",
            parse_mode="HTML"
        )

        return await print_message_state_change_mode(CREATE_TEST, TEACHER, context, chat_id)
