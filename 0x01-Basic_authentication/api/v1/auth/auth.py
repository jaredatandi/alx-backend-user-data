#!/usr/bin/env python3
"""Authentication module
"""


from flask import request
from typing import List, TypeVar
import fnmatch


class Auth:
    """Authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """routes that require auth

        Args:
            path (str): _description_
            excluded_paths (List[str]): _description_

        Returns:
            bool: _description_
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(path, excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Header data

        Args:
            request (_type_, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        if request is not None:
            return request.headers.get('Authorization', None)

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Determine user
        """
        return None
