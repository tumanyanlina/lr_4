import time
from functools import wraps

def log_func(func):
     @wraps(func)
     def wrapper(*args, **kwargs):
          print(f'[{time.strftime("%H:%M:%S")}] Вызов функции: [{func.__name__}]')
          return func(*args, **kwargs)
     return wrapper

@log_func
def my_func():
     print("hello, world")

my_func()
