#!/usr/bin/env python3
"""Basic auth module
"""

from api.v1.auth.auth import Auth
from models.user import User
from typing import Tuple, TypeVar
import base64


class BasicAuth(Auth):
    """Perform basic auth"""
    pass
