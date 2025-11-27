import time
from functools import wraps

def log_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'[{time.strftime("%H:%M:%S")}] Вызов функции: {func.__name__}()')
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'[{time.strftime("%H:%M:%S")}] Функция {func.__name__}() завершена за {end_time - start_time:.4f} сек')
        return result
    return wrapper
    
@log_func
def my_func():
    print("hello, world")

my_func()