import re

from marshmallow import ValidationError


class FileNameValidator:
    validator_error = "Filename contains inappropriate characters"
    extension_error = "Filename has unsupported extension"

    # Filename comes without extension
    def validate(self, filename):
        if not re.fullmatch(r"[0-9a-z]+", filename):
            raise ValidationError(self.validator_error)