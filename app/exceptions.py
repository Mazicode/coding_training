from flask import jsonify
from werkzeug.exceptions import HTTPException


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """
        Used in the actual error handling for `InvalidUsage`.
        """
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


def make_json_error(ex):
    response = jsonify(message=str(ex))
    response.status_code = (ex.code
                            if isinstance(ex, HTTPException)
                            else 500)
    return response
