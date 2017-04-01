import logging

__version__ = '1.1.0forkmp'

import sys
import os
sys.path.append(os.path.dirname(__file__))

try:
    import botocore120
except ImportError:
    logging.error('Impossible to find module botocore120.')

try:
    from .base import Botocore
except ImportError:
    logging.warning('It looks like some requirements are missing.')
