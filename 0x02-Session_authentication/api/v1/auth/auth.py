#!/usr/bin/env python3
'''
module for api authentication
'''
from flask import request
from typing import List, TypeVar

User = TypeVar('User')


class Auth:
    """
    class auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to require auth """
        if path is None:
            return True

        if not excluded_paths:
            return True

        # Add a trailing slash to path for uniformity
        if not path.endswith('/'):
            path += '/'

        # Check if path is in excluded_paths
        for excluded_path in excluded_paths:
            if excluded_path[-1] == '*':
                if path.startswith(excluded_path[:-1]):
                    return False
            elif path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method to get authorization header """
        if request is None:
            return None

        # Check if the request contains the 'Authorization' header
        if 'Authorization' not in request.headers:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> User:
        """ Method to get current user """
        return None

    def session_cookie(self, request=None) -> str:
        """
        Returns the value of the session cookie from the request.
        """
        if request is None:
            return None

        session_name = request.app.config.get("SESSION_NAME", "_my_session_id")
        return request.cookies.get(session_name)
