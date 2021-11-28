import re

from marshmallow import ValidationError


class PasswordValidator:
    password_check_error_msg = "Password should be at least 10 characters long, contain at least one lowercase, one uppercase character and one digit"

    def password_check(self, password):
        length_ok = len(password) >= 10
        lower_case_ok = re.search("[a-z]", password)
        upper_case_ok = re.search("[A-Z]", password)
        number_ok = re.search("[0-9]", password)
        if not (length_ok and lower_case_ok and upper_case_ok and number_ok):
            raise ValidationError(self.password_check_error_msg)
