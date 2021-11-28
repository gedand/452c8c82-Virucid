import re

from datab.database import User
from marshmallow import ValidationError


class UsernameValidator:
    username_check_error_msg = "Username should contain only English letters and numbers"
    username_taken_error_msg = "Username is taken"
    username_not_existing_msg = "Username does not exist"

    def username_register(self, username):
        if not re.fullmatch(r"[a-zA-Z0-9]+", username):
            raise ValidationError(self.username_check_error_msg)

        if User.query.filter_by(username=username).first():
            raise ValidationError(self.username_taken_error_msg)

    def username_login(self, username):
        if not re.fullmatch(r"[a-zA-Z0-9]+", username):
            raise ValidationError(self.username_check_error_msg)
