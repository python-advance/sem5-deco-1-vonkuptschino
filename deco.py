def deco(func):
  import time
  import functools
  import math 

  @functools.wraps(func)
  def inner(*args, **kwargs):
    start = time.time()
    res = func(*args, **kwargs)
    finish = time.time()

    delta = (finish - start)
    print(f'{func.__name__} works for {delta:2.3}')
    return res
  return  inner
