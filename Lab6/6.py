from decorator import log_exceptions
@log_exceptions
def divide(a, b):
    return a / b

divide(5, 0) 
