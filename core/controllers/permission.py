from db.permissions import User


class PermissionController:

    def __init__(self, user: User):
        self._user = user

    @property
    def user(self) -> User:
        return self._user

    @staticmethod
    def get_user_by_telegram_id(telegram_id: int) -> 'PermissionController':
        user, _ = User.get_or_create(telegram_id=telegram_id)
        return PermissionController(user)
