import flask
from flask import Request
import badgettingbetter.infrastructure.request_dict as request_dict
import bson

from typing import Optional

class ViewModelBase:
    def __init__(self):
        self.request: Request = flask.request
        self.request_dict = request_dict.create('')

        self.error: Optional[str] = None

    def to_dict(self):
        return self.__dict__
