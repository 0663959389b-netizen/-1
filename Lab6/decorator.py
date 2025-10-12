import traceback

def log_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)  # спробувати виконати оригінальну функцію
        except Exception as e:
            with open("errors.log", "a", encoding="utf-8") as f:  # відкрити файл у режимі додавання
                f.write(f"Exception in function '{func.__name__}': {e}\n")
                f.write(traceback.format_exc())  # записати повний трейсбек помилки
                f.write("\n" + "-"*40 + "\n")
            raise  # пробросити помилку далі, якщо треба
    return wrapper
