from telegram import User as TelegramUser

from db.permissions import User


class PermissionController:

    def __init__(self, user: User):
        self._user = user

    @property
    def user(self) -> User:
        return self._user

    @staticmethod
    def get_user_by_telegram(telegram_user: TelegramUser) -> 'PermissionController':
        user, _ = User.get_or_create(telegram_id=telegram_user.id)
        user.name = telegram_user.full_name
        user.save()
        return PermissionController(user)
