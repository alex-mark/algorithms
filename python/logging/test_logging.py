import logging
import employee

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("test_logging.log")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception("Tried to divide by zero")
    else:
        return result


num_1 = 20
num_2 = 0


add_res = add(num_1, num_2)
logger.debug(f"Add: {num_1} + {num_2} = {add_res}")

sub_result = subtract(num_1, num_2)
logger.debug(f"Sub: {num_1} - {num_2} = {add_res}")

mul_res = multiply(num_1, num_2)
logger.debug(f"Mul: {num_1} * {num_2} = {add_res}")

div_res = divide(num_1, num_2)
logger.debug(f"Div: {num_1} / {num_2} = {add_res}")
