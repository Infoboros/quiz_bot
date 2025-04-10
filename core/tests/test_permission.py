from core.controllers.permission import PermissionController
from db.permissions import User


def test_get_user(telegram_id):
    controller = PermissionController.get_user_by_telegram_id(telegram_id)

    assert type(controller) is PermissionController
    assert User.get(telegram_id=telegram_id).telegram_id == controller.user.telegram_id

    controller.user.delete_instance()
