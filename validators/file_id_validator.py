from marshmallow import ValidationError


class FileIdValidator:
    file_id_error = "File id cannot be negative number"

    def validate(self, file_id):
        if file_id < 1:
            raise ValidationError(self.validator_error)
