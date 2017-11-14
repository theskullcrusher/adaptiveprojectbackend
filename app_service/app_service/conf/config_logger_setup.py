import os
import logging

from app_service.conf.environments import get_config

log_format = ' '.join([
    '[%(asctime)s]',
    '[%(process)d-%(thread)d]',
    '%(levelname)s',
    '-',
    '%(message)s'
])

formatter = logging.Formatter(log_format)

def setup_config_logger(app):
    app.secret_key = "22ca4c58-09ab-46c6-bf1c-d26e626g2s32"
    app_env = os.environ.get('APP_ENV', 'local')
    config = get_config(app_env)
    app.config.from_object(config)
    app.debug_log_format = log_format

    if not app.debug:
        logHandler = logging.StreamHandler()

        logHandler.setFormatter(formatter)
        logHandler.setLevel(logging.DEBUG)
        app.logger.addHandler(logHandler)
        app.logger.setLevel(logging.DEBUG)

    app.logger.info("Loaded environment: " + app_env)
