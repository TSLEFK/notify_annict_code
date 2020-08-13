import json
import logging
import os

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

class JsonFormatter:
    def format(self, record):
        return json.dumps(vars(record))

def get_logger(name: str):
    logging.basicConfig()
    handler = logging.StreamHandler()
    handler.setFormatter(JsonFormatter)

    logger = logging.getLogger(name=name)
    logger.addHandler(hdlr=handler)
    logger.setLevel(LOG_LEVEL)

    return logger



