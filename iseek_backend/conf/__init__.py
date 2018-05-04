import os
from .logs import *
if os.getenv("ISEEK_BACKEND_ENV") == "prod":
    # 线上环境
    from .prod import *
    DEBUG = False
    ALLOWED_HOSTS = ["*"]
else:
    # 开发环境
    from .dev import *
    DEBUG = True
