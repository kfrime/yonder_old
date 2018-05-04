# -*- coding:utf-8 -*-

# log 的配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
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
            'backupCount': '5'
        },
        'operatelog': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': 'log/operate.log',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': '5'
        },
        'sqllog': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': 'log/sql.log',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': '5'
        }
    },
    'loggers': {
        'info': {
            'handlers': ['infolog'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'operate': {
            'handlers': ['operatelog'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['sqllog'],
        }
    }
}
