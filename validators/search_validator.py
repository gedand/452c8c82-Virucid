import datetime
from marshmallow import ValidationError

class SearchValidator:
    validator_error = "Filename contains inappropriate characters"

    def validate_date(self, date):
        if not datetime.datetime.strptime(date, '%Y-%m-%d'):
            raise ValidationError(self.validator_error)