from telegram import Update
from telegram.ext import CallbackContext, CallbackQueryHandler


def create_callback_to_state(print_message_state_change):
    async def callback(update: Update, context: CallbackContext):
        query = update.callback_query
        await query.answer()
        return await print_message_state_change(context, query.message.chat.id)

    return CallbackQueryHandler(callback)
