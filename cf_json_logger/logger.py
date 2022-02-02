import logging

from cf_json_logger.cf_json_formatter import CarnallFarrarJsonFormatter


def get_logger() -> logging.Logger:
    logging.getLogger("werkzeug").setLevel(logging.ERROR)
    logging.getLogger("boto3").setLevel(logging.INFO)
    logging.getLogger("botocore").setLevel(logging.INFO)
    logging.getLogger("s3transfer").setLevel(logging.INFO)
    logging.getLogger("urllib3").setLevel(logging.INFO)
    logging.getLogger("uvicorn").setLevel(logging.INFO)

    logging.addLevelName(logging.ERROR, "error")
    logging.addLevelName(logging.WARNING, "warning")
    logging.addLevelName(logging.INFO, "info")
    logging.addLevelName(logging.DEBUG, "debug")

    logger = logging.getLogger()
    logHandler = logging.StreamHandler()

    formatter = CarnallFarrarJsonFormatter("%(asctime)s %(level)s %(pathname)s %(module)s %(processName)s %(message)s")

    logHandler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)

    logger.addHandler(logHandler)

    return logger
