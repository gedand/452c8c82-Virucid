from datab.database import User


class UserHelper:

    def get_user(username="", id=""):
        if not username and not id:
            raise Exception("Incorrect parameters for get_user function")
        if username:
            user = User.query.filter_by(username=username).first()
        else:
            user = User.query.get(id)
        if user is None:
            raise ValueError('User does not exist')
        return user
