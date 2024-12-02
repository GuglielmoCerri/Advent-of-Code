import logging
from logging import config
from pathlib import Path

FORMAT_STRING = '%(asctime)s [%(levelname)s] %(filename)s - %(message)s'

LOG_CONFIG = {
    "version":1,
    "disable_existing_loggers": False,
    "root":{
        "handlers" : ["file"],
        "level": "DEBUG"
    },  
    "handlers":{
        "file":{
            "formatter": "std_out",
            "class": "logging.FileHandler",
            "level": "DEBUG",
            'mode': 'a+', 
        },
    },
    "formatters":{
        "std_out": {
            "format": FORMAT_STRING,
            "datefmt":"%d-%m-%Y %H:%M:%S"
        },
    },
}

def config_log(LOG_PATH):
    
    LOG_CONFIG['handlers']['file']['filename'] = LOG_PATH
    
    config.dictConfig(LOG_CONFIG)
    logger = logging.getLogger(__name__)
    
    return logger