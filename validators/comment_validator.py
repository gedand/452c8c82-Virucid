from marshmallow import ValidationError


class CommentValidator:
    file_id_error = "File id cannot be negative number"
    comment_long = "Comment is too long"
    comment_empty = "Comment is empty"

    def file_id_validate(self, file_id):
        if file_id < 1:
            raise ValidationError(self.validator_error)
    
    # SQLAlchemy escapes character during query, here we check only length
    def comment_validate(self, comment):
        comment_len = len(comment)
        if comment_len >=5000:
            raise ValidationError(self.comment_long)
        if comment_len <=0:
            raise ValidationError(self.comment_empty)