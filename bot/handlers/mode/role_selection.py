from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from bot.handlers.states import STUDENT, TEACHER
from bot.keyboard.select_role import get_select_role_keyboard
from bot.keyboard.select_student_action import get_select_student_action_keyboard


async def role_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('role selection')
    query = update.callback_query
    await query.answer()
    role = query.data
    context.user_data["role"] = role
    if role == "teacher":
        print('Teacher')
        await query.edit_message_text(
            text="Вы выбрали роль Учитель.\nДля создания теста отправьте название теста."
        )
        return TEACHER
    elif role == "student":
        print('Student')
        await query.edit_message_text(
            text="Вы выбрали роль Ученик.\n",
            reply_markup=get_select_student_action_keyboard()
        )
        return STUDENT
    else:
        await query.edit_message_text(text="Неизвестная роль. Попробуйте ещё раз.")
        return ConversationHandler.END