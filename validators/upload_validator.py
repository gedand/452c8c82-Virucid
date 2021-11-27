from marshmallow import ValidationError


class UploadValidator:
    validator_error = "File is needed"

    def validate(self, file):
        # print('len:')
        # print(len(file))
        if not file:
            raise ValidationError(self.validator_error)