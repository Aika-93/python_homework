#Task_1: Writing and Testing a Decorator

import logging 

def logger_decorator(func):
    logger = logging.getLogger(func.__name__ + "_parameter_log")
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.FileHandler("./decorator.log","a"))
    logger.log(logging.INFO, "this string would be logged")
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        pos_args = args if args else "none"
        kw_args = kwargs if kwargs else "none"

        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {pos_args}")
        logger.log(logging.INFO, f"keyword parameters: {kw_args}")
        logger.log(logging.INFO, f"return: {result}")
        return result
    return wrapper

@logger_decorator
def example():
    return "Hello World"

@logger_decorator
def arguments(*args):
    return True

@logger_decorator
def return_decorator(**kwargs):
    return logger_decorator

example()
arguments(5,7,8)
return_decorator(name = "Aiperi", age = 32)