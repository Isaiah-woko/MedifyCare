from .models import Message
from flask_login import current_user
from .. import db


def save_message(receiver_id, content):
    message = Message(sender_id=current_user.id, receiver_id=receiver_id, content=content)
    db.session.add(message)
    db.session.commit()
    return message


def get_messages(user_id1, user_id2):
    return Message.query.filter(
        ((Message.sender_id == user_id1) & (Message.receiver_id == user_id2)) |
        ((Message.sender_id == user_id2) & (Message.receiver_id == user_id1))
    ).order_by(Message.timestamp.asc()).all()
