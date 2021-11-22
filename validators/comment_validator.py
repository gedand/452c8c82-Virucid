from marshmallow import ValidationError


class CommentValidator:
    comment_long = "Comment is too long"
    comment_empty = "Comment is empty"

    # SQLAlchemy escapes character during query, here we check only length
    def validate(self, comment):
        comment_len = len(comment)
        if comment_len >=5000:
            raise ValidationError(self.comment_long)
        if comment_len <=0:
            raise ValidationError(self.comment_empty)