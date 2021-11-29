from marshmallow import ValidationError
from werkzeug.utils import secure_filename


class UploadValidator:
    validator_error = "File has unsupported extension"


    def validate(self, file):
        if not file:
            raise ValidationError(self.validator_error)

        filename = secure_filename(file.filename)
        try:
            extension = filename.split('.')[1]
        except IndexError:
            raise ValueError("Input format is not in correct form")

        if extension != 'caff':
            raise ValidationError(self.validator_error)
