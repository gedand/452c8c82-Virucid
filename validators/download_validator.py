import re
from marshmallow import ValidationError


class DownloadValidator:
    validator_error = "Filename contains inappropriate characters"
    extension_error = "Filename has unsupported extension"

    def  validate(self, filename):
        name_trimmed = filename.split('.')[0]
        extension = filename.split('.')[1]
        if not re.fullmatch(r"[0-9a-z]+", name_trimmed):
            raise ValidationError(self.validator_error)
        accepted_extensions = ['jpg', 'jpeg', 'png', 'caff', 'txt'] # TODO: .txt majd kiszed
        if extension not in accepted_extensions:
            raise ValidationError(self.extension_error)