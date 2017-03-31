import logging

__version__ = '1.1.0fork'

try:
    from .base import Botocore
except ImportError:
    logging.warning('It looks like some requirements are missing.')
