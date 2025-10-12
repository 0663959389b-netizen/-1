def log_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            with open("errors.log", "a", encoding="utf-8") as f:
                f.write(f"Помилка у функції {func.__name__}: {e}\n")
            raise  # піднімаємо помилку далі
    return wrapper

