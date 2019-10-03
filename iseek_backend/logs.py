# -*- coding:utf-8 -*-

# log 的配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            # 日期和时间 	文本格式的日志级别 进程ID:线程ID 记录器的名称 模块名称:函数名称:行号 记录的消息
            'format': '%(asctime)s [%(levelname)s] [%(process)d:%(thread)d] [%(name)s] [%(module)s.%(funcName)s:%(lineno)d] - %(message)s'
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'infolog': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': 'log/info.log',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 5
        },
        'operatelog': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': 'log/operate.log',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 5
        },
        'sqllog': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': 'log/sql.log',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 5
        }
    },
    'loggers': {
        # 本Django后端被动接受请求URL时产生的配置
        'info': {
            'handlers': ['infolog'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # 本后端主动请求其他URL时可以用下面的配置
        'operate': {
            'handlers': ['operatelog'],
            'propagate': False,
            'level': 'DEBUG',
        },
        # 本后端产生SQL的log
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['sqllog'],
        }
    }
}
