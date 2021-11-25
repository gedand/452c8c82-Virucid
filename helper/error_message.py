from flask import current_app as app


class ErrorMessage:
    def OK_content(content):
        return {
                   content
               }, 200

    def OK(message=""):
        return {
                   "status": "success",
                   "message": message
               }, 200

    def bad_request(message="Invalid request"):
        return {
                   "status": "error",
                   "message": message
               }, 400

    def forbidden(message="You don't have enough permission"):
        return {
                   "status": "error",
                   "message": message
               }, 403

    def server(message="Server error"):
        return {
                   "status": "error",
                   "message": message
               }, 500
