from testfixtures import LogCapture

from cf_json_logger import get_logger


def test_get_logger():
    """
    GIVEN
    WHEN logger.info is called
    THEN python logger is returned
    """
    logger = get_logger()

    assert logger is not None


def test_logger_info():
    """
    GIVEN
    WHEN logger.info is called
    THEN message is shown
    """
    logger = get_logger()

    with LogCapture() as capture:
        logger.info("Test Output")

    capture.check(("root", "info", "Test Output"))
