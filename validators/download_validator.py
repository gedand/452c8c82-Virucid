import re
from marshmallow import ValidationError


class DownloadValidator:
    validator_error = "Filename contains not only digits"

    def  validate(self, filename):
        trimmed = filename.split('.')[0]
        if not re.fullmatch(r"[0-9]+", trimmed):
            raise ValidationError(self.validator_error)