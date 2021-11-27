from marshmallow import ValidationError
import re


class FileNameValidator:
    validator_error = "Filename contains inappropriate characters"
    extension_error = "Filename has unsupported extension"

    def validate(self, filename):
        try:
            name_trimmed = filename.split('.')[0]
            extension = filename.split('.')[1]
        except IndexError:
            raise ValueError("Input format is not in correct form")
            
        if not re.fullmatch(r"[0-9a-z]+", name_trimmed):
            raise ValidationError(self.validator_error)
        accepted_extensions = ['jpg', 'jpeg', 'png']
        if extension not in accepted_extensions:
            raise ValidationError(self.extension_error)
