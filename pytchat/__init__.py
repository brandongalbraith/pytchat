"""
pytchat is a python library for fetching youtube live chat.
"""
__copyright__    = 'Copyright (C) 2019 taizan-hokuto'
__version__      = '0.0.1.7'
__license__      = 'MIT'
__author__       = 'taizan-hokuto'
__author_email__ = '55448286+taizan-hokuto@users.noreply.github.com'
__url__          = 'https://github.com/taizan-hokuto'

__all__ = ["core_async","core_multithread","processors"]

from .api import (
    LiveChat,
    LiveChatAsync,
    CompatibleProcessor, 
    SimpleDisplayProcessor,
    JsonfileArchiveProcessor
    )