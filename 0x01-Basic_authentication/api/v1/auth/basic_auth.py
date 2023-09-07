#!/usr/bin/env python3
"""Basic auth module
"""

from api.v1.auth.auth import Auth
from models.user import User
from typing import Tuple, TypeVar
import base64
import re
import binascii

from .auth import Auth
from models.user import User


class BasicAuth(Auth):
    """Perform basic auth"""

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        if authorization_header is None:
            return None

        if type(authorization_header) == str:
            pattern = r'Basic (?<token>.+)'
            match_pattern = re.fullmatch(pattern, authorization_header.strip())
            if match_pattern is not None:
                return match_pattern.group('token')
        return None
