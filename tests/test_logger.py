from cf_json_logger import get_logger

from testfixtures import LogCapture

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

    with LogCapture() as l:
        logger.info("Test Output")

    l.check(
        ('root', 'info', 'Test Output')
    )
