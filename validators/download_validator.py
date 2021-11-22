import re
from marshmallow import ValidationError


class DownloadValidator:
    validator_error = "Filename contains inappropriate characters"

    def  validate(self, filename):
        trimmed = filename.split('.')[0]
        if not re.fullmatch(r"[0-9a-z]+", trimmed):
            raise ValidationError(self.validator_error)