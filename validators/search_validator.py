import re
import datetime
from marshmallow import ValidationError

class SearchValidator:
    validator_error = "Filename contains inappropriate characters"

    def validate_date(self, date):
        print(date)
        if not datetime.datetime.strptime(date, '%Y-%m-%d'):
            raise ValidationError(self.validator_error)
        # if not re.fullmatch(r"[0-9a-z]+", trimmed):
        #     raise ValidationError(self.validator_error)