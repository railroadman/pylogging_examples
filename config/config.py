log_config = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'WARN',
            'formatter': 'standard',
        },
        'logfile': {
            'class': 'logging.FileHandler',
            'filename': 'logs/dict_log.log',
            'formatter': 'standard',
            
        }

    },

    'loggers': {
        'root': {
        'handlers': ['logfile','console'],
    },
        'myapp': {
            'level': 'DEBUG',
            'handlers': ['logfile','console']
        }   
    },

    
}