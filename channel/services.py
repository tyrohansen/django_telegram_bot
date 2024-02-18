
from channel.models import MenuOptions, Menus, Session


def get_session(chat_id):
    return Session.objects.filter(chat_id=chat_id, is_closed=False).last()

def create_user_session(chat_id, msg_id, message, menu_id):
    session = Session.objects.create(
        chat_id=chat_id,
        menu_id=menu_id,
        last_text=message,
        msg_id=msg_id
    )
    return session

def get_default_menu():
    return Menus.objects.filter(parent__isnull=True).first()


def get_menu(parent_id):
    return Menus.objects.filter(parent_id=parent_id).first()


def get_menu_options(menu_id):
    return MenuOptions.objects.filter(menu_id=menu_id).all()