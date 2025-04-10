from db.permissions import User


class PermissionController:

    def __init__(self, user: User):
        self.user = user

    @staticmethod
    def get_user_by_telegram_id(telegram_id: int) -> 'PermissionController':
        user, _ = User.get_or_create(telegram_id=telegram_id)
        return PermissionController(user)
