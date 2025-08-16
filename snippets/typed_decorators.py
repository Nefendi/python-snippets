from collections.abc import Callable
from functools import wraps
from typing import overload


@overload
def decorator[ReturnType, **Params](
    func: Callable[Params, ReturnType],
) -> Callable[Params, ReturnType]: ...


@overload
def decorator[ReturnType, **Params](
    func: None = ...,
) -> Callable[[Callable[Params, ReturnType]], Callable[Params, ReturnType]]: ...


# Can be called with or without parentheses
def decorator[ReturnType, **Params](
    func: Callable[Params, ReturnType] | None = None,
) -> (
    Callable[[Callable[Params, ReturnType]], Callable[Params, ReturnType]]
    | Callable[Params, ReturnType]
):
    def inner(
        func: Callable[Params, ReturnType],
    ) -> Callable[Params, ReturnType]:
        @wraps(func)
        def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> ReturnType:
            print("Before")
            res = func(*args, **kwargs)
            print("After")

            return res

        return wrapper

    if func is None:
        return inner

    return inner(func)


@overload
def decorator_with_params[ReturnType, **Params](
    func: Callable[Params, ReturnType], *, param: bool = ...
) -> Callable[Params, ReturnType]: ...


@overload
def decorator_with_params[ReturnType, **Params](
    func: None = ..., *, param: bool = ...
) -> Callable[[Callable[Params, ReturnType]], Callable[Params, ReturnType]]: ...


# Can be called with or without parentheses
def decorator_with_params[ReturnType, **Params](
    func: Callable[Params, ReturnType] | None = None, *, param: bool = True
) -> (
    Callable[[Callable[Params, ReturnType]], Callable[Params, ReturnType]]
    | Callable[Params, ReturnType]
):
    def inner(
        func: Callable[Params, ReturnType],
    ) -> Callable[Params, ReturnType]:
        @wraps(func)
        def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> ReturnType:
            print("Before")
            print(f"Value of param = {param}")
            res = func(*args, **kwargs)
            print("After")

            return res

        return wrapper

    if func is None:
        return inner

    return inner(func)


@decorator
def func(a: int, b: int) -> None:
    print(a, b)


@decorator()
def func2(a: int, b: int) -> None:
    print(a, b)


@decorator_with_params(param=True)
def func3(a: int, b: int) -> None:
    print(a, b)


@decorator_with_params
def func4(a: int, b: int) -> None:
    print(a, b)


@decorator_with_params()
def func5(a: int, b: int) -> None:
    print(a, b)


func(1, 2)
print()
func2(1, 2)
print()
func3(1, 2)
print()
func4(1, 2)
print()
func5(1, 2)
