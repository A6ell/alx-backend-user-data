#!/usr/bin/env python3
"""
Auth class
"""

from flask import request
from typing import TypeVar, List
from os import getenv

User = TypeVar('User')


class Auth:
    """
    A class to manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns False if path is in excluded_paths.
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            path += "/"
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the value of the Authorization header from a request.
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> User:
        """
        Returns None for the current user.
        """
        return None

    def session_cookie(self, request=None):
        """
        Returns a cookie value from a request.
        """
        if request:
            session_name = getenv("SESSION_NAME", "_my_session_id")
            return request.cookies.get(session_name, None)
        return None
