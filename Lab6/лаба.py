from decorator import log_exceptions

@log_exceptions
def divide(a, b):
    return a / b

if __name__ == '__main__':
    divide(5, 0)
