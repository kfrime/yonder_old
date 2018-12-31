# -*- coding:utf-8 -*-

# log 的配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            # 日期和时间 	文本格式的日志级别 进程ID 模块名称:函数名称:行号 记录的消息
            'format': '[%(asctime)s]-[%(levelname)s]-[%(process)d]-[%(module)s.%(funcName)s:%(lineno)d]:: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
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
        'info_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'verbose',
            'filename': 'logs/info.log',
            'when': 'D',
        },
        'sql_log': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'verbose',
            'filename': 'logs/sql.log',
            'when': 'D',
        }
    },
    'loggers': {
        # 处理请求的log
        'info': {
            'handlers': ['info_log'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # Django产生SQL的log
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['sql_log'],
        }
    }
}
