# -*- coding:utf-8 -*-

import os
from .base import *
from .logs import *

if os.getenv("SERVER_ENV") == "production":
    DEBUG = False


