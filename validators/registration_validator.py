from marshmallow import ValidationError
import re
from datab.database import User

class RegistrationValidator:
    username_check_error_msg = "Username should contain only English letters and numbers"
    password_check_error_msg = "Password should be at least 10 characters long, contain at least one lowercase, one uppercase character and one digit"
    username_taken_error_msg = "Username is taken" 

    def username_check(self, username):
        if not re.fullmatch(r"[a-zA-Z0-9]+", username):
            raise ValidationError(self.username_check_error_msg)
        
        if User.query.filter_by(username=username).first():
            raise ValidationError(self.username_taken_error_msg)

    def password_check(self, password):
        length_ok = len(password) >= 10
        lower_case_ok = re.search("[a-z]", password)
        upper_case_ok = re.search("[A-Z]", password)
        number_ok = re.search("[0-9]", password)
        if not (length_ok and lower_case_ok and upper_case_ok and number_ok):
                raise ValidationError(self.password_check_error_msg)