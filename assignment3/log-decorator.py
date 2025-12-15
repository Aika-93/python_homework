#Task_1: Writing and Testing a Decorator

import logging 

def logger_decorator(func):
    logger = logging.getLogger(func.__name__ + "_parameter_log")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        logger.addHandler(logging.FileHandler("./decorator.log","a"))

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        pos_args = args if args else "none"
        kw_args = kwargs if kwargs else "none"

        log_message = (
            f"function: {func.__name__}\n"
            f"positional parameters: {pos_args}\n"
            f"keyword parameters: {kw_args}\n"
            f"return: {result}\n"
        )
        logger.log(logging.INFO, log_message)
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