## What are Python Decorators?
Python decorators are a design pattern that allows us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.

### Key Concepts
- **Decorators as Functions**: A decorator is a function that takes another function as an argument and extends its behavior without changing its source code.
- **Wrapper Functions**: The decorator function creates a new function (the wrapper) that "wraps" the original function, allowing us to modify its behavior.
- **Metadata**: Decorators can also be used to add metadata to functions, such as documentation strings or type hints.

### Simple Example
```python
# Define a decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Apply the decorator to a function
@my_decorator
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()
```
In this example, the `my_decorator` function is a decorator that takes the `say_hello` function as an argument. The decorator creates a new function `wrapper` that "wraps" the original `say_hello` function, allowing us to modify its behavior. When we call `say_hello()`, it actually calls the `wrapper` function, which prints the additional messages before and after calling the original `say_hello` function.