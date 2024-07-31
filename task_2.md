Write a decorator in python that will count how many times the decorated function was called. It should print the number every time the decorated function is executed. Each function should be counted separately.

Answer:


Copy and paste this decorator declaration in a Python interpreter:

```python

def function_counter(func):

    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"{func.__name__} has been invoked {wrapper.count} time{'s' if wrapper.count > 1 else ''}")
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper
```

Then, apply this decorator to any function you want to count:

```python
@function_counter
def first_function():
    print("First function")


@function_counter
def second_function():
    print("Second function")


@function_counter
def third_function():
    print("Third function")
```

Then, invoke the functions and observe the counter increasing:

```python
>>> first_function()
First function
first_function has been invoked 1 time.

>>> first_function()
First function
first_function has been invoked 2 times.

>>> first_function()
First function
first_function has been invoked 3 times.
```