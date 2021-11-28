from datab.database import User
from datab.shared import db
from flask import current_app as app

from helper.password_helper import PasswordHelper


class AdminHelper:
    @staticmethod
    def add_admin_user():
        admin_username = 'admin'
        if not User.query.filter_by(username=admin_username).first():
            with open('config/admin_pass', 'r') as file:
                admin_pass = file.read().rstrip()

            password_hash, salt = PasswordHelper.hash_register(admin_pass)
            guest = User(username=admin_username, password=password_hash, salt=salt, is_admin=1)
            db.session.add(guest)
            db.session.commit()
